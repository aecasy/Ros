#!/usr/bin/env python3

# This function asks the robot for its speed profile, 
# and publishes it in plaintext, without ant converter (translation)
# the format of the published message <x> <y> <z> <w1> <w2> <w3> <w4>. 
# where w stands for wheel

# By Meshi Blum
# 21.7.21

# To Do
# later, it may be right to change the String into Twist type, 
# and change the script a bit accordingly
import socket
import sys
import rospy
from std_msgs.msg import String

# In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
#host = "192.168.2.1"
#port = 40923

#address = (host, int(port))
# Establish a TCP connection with the control command port of the robot.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print("Connecting...")
#s.connect(address)
#print("Connected!")
# initiate the robot
#msg = "command;"
#s.send(msg.encode('utf-8'))

def publisher():
    
    pub = rospy.Publisher('speed_info', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = 'chassis speed ?;'
        s.send(msg.encode('utf-8'))
        info = str(s.recv(1024))
        print(info)
        pub.publish(info)
        rate.sleep()

    # Disconnect the port connection.
    s.shutdown(socket.SHUT_WR)
    s.close()
    
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass