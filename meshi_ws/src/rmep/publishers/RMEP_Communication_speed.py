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
host = "192.168.42.2"
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

if __name__ == '__main__':
    listener()



