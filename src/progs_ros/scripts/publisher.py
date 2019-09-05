#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node('talker', anonymous=True)

    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        i = 0
        hello_str = "Oi, estou publicando_" + str(i)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i = i+1

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass