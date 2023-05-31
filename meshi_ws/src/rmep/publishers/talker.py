#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)
    # position speed attitude angular rate
    cnt=0
    while not rospy.is_shutdown():
        print('SCNT ' + str(cnt))
        cnt=cnt+1
        messages="chassis speed ?"
        pub.publish(messages)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
