 #!/usr/bin/env python3

# This function subscribes to 'velocity' topic published by simulink, 
# and publishes it in plaintext, after going through the converter

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import socket
import sys
from datetime import datetime
import pickle
from time import sleep

# In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
host = "192.168.2.1"
port = 40923

address = (host, int(port)) 
# Establish a TCP connection with the control command port of the robot.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
s.connect(address)
print("Connected!")
# initiate the robot
msg = "command;"
s.send(msg.encode('utf-8'))

delayplot=[]
recieve_counter_liran=0


def convertdata(data):
    global delayplot
    global recieve_counter_liran
    
    # transforms the data recieved from simulink to string form
    angular = str(data.angular).replace("\n"," ").replace(':','').split('z')

    linear = str(data.linear).replace("\n"," ").replace(':','')
    x_speed = linear.split('x')[1].split('y')[0]
    y_speed = linear.split('y')[1].split('z')[0]

    z_angular = angular[1]
    # the final command in plaintext format
    new_msg = 'chassis speed x%sy%sz%s' %(x_speed, y_speed, z_angular)
    recieve_counter_liran = recieve_counter_liran+1
    print(recieve_counter_liran)

    msg = new_msg
    # Add the ending character.
    msg += ';'
    # Send control commands to the robot.
    print(msg)
    start=datetime.now()
    s.send(msg.encode('utf-8'))
    try:
            # Wait for the robot to return the execution result.
            buf = s.recv(1024)
            time_diff=(datetime.now()-start).total_seconds()*1000
            #print("Delay: %sms" %time_diff)
            delayplot.append(time_diff)
            with open('outfile', 'wb') as fp:
                pickle.dump(delayplot, fp)
            
    except socket.error as e:
            print("Error receiving :", e)
            sys.exit(1)
    
    
def listener():
    rospy.init_node('msg', anonymous=True)
    rospy.Subscriber("velocity", Twist, convertdata)
    rospy.spin()
    
    # Disconnect the port connection.
    s.shutdown(socket.SHUT_WR)
    s.close()
RPMplot=[]
RPMCommand=[]
timevalues=[]
def dostuff():
    global RPMplot
    global RPMCommand
    global timevalues
    start=datetime.now()
    
    switched=False
    switched2=False
    while (datetime.now()-start).total_seconds()<8:
        timevalues.append((datetime.now()-start).total_seconds()*1000)
        if (datetime.now()-start).total_seconds()>5:
            if not switched:
                print((datetime.now()-start).total_seconds())
                switched=True
                s.send("chassis wheel w1 0;".encode('utf-8'))
                try:
                    buf = s.recv(1024).decode('utf-8')
                except socket.error as e:
                    print("Error receiving :", e)
                    sys.exit(1)
                print((datetime.now()-start).total_seconds())
            RPMCommand.append(0)
        else:
            if not switched2:
                switched2=True
                s.send("chassis wheel w1 600;".encode('utf-8'))
                try:
                    buf = s.recv(1024).decode('utf-8')
                except socket.error as e:
                    print("Error receiving :", e)
                    sys.exit(1)
            RPMCommand.append(600)
            
        s.send(("chassis speed ?;").encode('utf-8'))
        try:
            print((datetime.now()-start).total_seconds())
            buf = (s.recv(1024).decode('utf-8')).split()
            print((datetime.now()-start).total_seconds())
            if buf!=['ok;']:
                rpm=buf[3]
                RPMplot.append(rpm)
                
            else:
                print("this shit again")
                RPMplot.append('100')
        except socket.error as e:
            print("Error receiving :", e)
            sys.exit(1)
        

    with open('outfile', 'wb') as fp:
        pickle.dump(RPMCommand, fp)
    with open('outfile3', 'wb') as fp3:
        pickle.dump(timevalues, fp3)
    with open('outfile2', 'wb') as fp2:
        pickle.dump(RPMplot, fp2)

if __name__ == '__main__':
    dostuff()



