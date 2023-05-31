#!/usr/bin/env python3

# Revision $Id$


import socket
import sys
import rospy
from std_msgs.msg import String,Int32,Int16MultiArray,MultiArrayLayout,MultiArrayDimension
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

def wheeldatapublisher():
    pub = rospy.Publisher('wheeldata', Int16MultiArray, queue_size=10) 
    rospy.init_node('publishwheeldatanode', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        msg="chassis wheel ?"
        msg+=";"
        s.send(msg.encode('utf-8'))
        
        try:
            answer = s.recv(1024).decode('utf-8')
            if answer!="ok;":
                a=Int16MultiArray()
                print(answer)
                print(type(int(answer.split()[0])))
                a.data=[int(answer.split()[0]),int(answer.split()[1]),int(answer.split()[2]),int(answer.split()[3])]
                pub.publish(a)
        except socket.error as e:
            print("Error receiving (Liran) :", e)
            sys.exit(1)
        rate.sleep()

if __name__ == '__main__':
    try:
        wheeldatapublisher()
    except rospy.ROSInterruptException:
        pass
