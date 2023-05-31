#!/usr/bin/env python3

# This function activates RM through SDK and sends RM the data 
# publihed by the meshi_converter

# By Meshi Blum
# 19.7.21

import socket
import sys
import rospy
from std_msgs.msg import String

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

def callback(data):
    msg = data.data
    # Add the ending character.
    msg += ';'
    # Send control commands to the robot.
    s.send(msg.encode('utf-8'))
    try:
            # Wait for the robot to return the execution result.
            buf = s.recv(1024)
    except socket.error as e:
            print("Error receiving :", e)
            sys.exit(1)

def subscriber():
    rospy.init_node('RMEP', anonymous=True)
    rospy.Subscriber("Demo", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    # Disconnect the port connection.
    s.shutdown(socket.SHUT_WR)
    s.close()

if __name__ == '__main__':
    subscriber()