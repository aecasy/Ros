#!/usr/bin/env python3

# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import socket
import sys
import rospy
from std_msgs.msg import String
from datetime import datetime

# In direct connection mode, the default IP address of the robot is 192.168.2.1 
# and the control command port is port 40923.
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
recieve_counter_liran=0
start=datetime.now()

def callback(data):

    global recieve_counter_liran
    recieve_counter_liran = recieve_counter_liran+1
    time_diff=(datetime.now()-start).total_seconds()
    frequency=recieve_counter_liran/time_diff
    print("frequency of data received: "+str(round(frequency, 2))+"Hz")
    #print("frequency of data received: "+str(frequency)+"Hz")
    
    # answer=[]
    # i=0
    # messages = data.data
        # messages=[
        #     "chassis speed ?",
        #     "chassis position ?",
        #     ]
        # rospy.loginfo(messages[0])
        # pub.publish(messages[0])
        # pub.publish(messages[1])
        # rate.sleep()
    # for msg in messages:
    #     msg += ';'
    #     s.send(msg.encode('utf-8'))
    #     try:
    #         answer.append = s.recv(1024)
    #         answer[i].decode('utf-8')
    #     except socket.error as e:
    #         print("Error receiving (Liran) :", e)
    #         sys.exit(1)
    #     i=i+1

    # ans=["chassis speed vector: ", "chassis position vector: "]
    # print(ans[i]+answer)



    messages = data.data
    messages +="*"
    
    separator=messages.find('*')
    msgindex=0
    msgreply=["chassis speed vector: ", "chassis position vector: ", "chassis attitude vector: "]

    while separator != -1:
        msg=messages[:separator]
        msg+=";"
        s.send(msg.encode('utf-8'))
        
        messages=messages[separator+1:len(messages)]
        
        try:
            answer = s.recv(1024).decode('utf-8')
            print(msgreply[msgindex]+answer)
            print(answer.split()[1])
        except socket.error as e:
            print("Error receiving (Liran) :", e)
            sys.exit(1)
        separator=messages.find('*')
        msgindex+=1


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
