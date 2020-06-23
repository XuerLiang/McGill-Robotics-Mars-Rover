#!/usr/bin/env python2

import rospy
from beginner_tutorials.msg import ControlOutput

def fake_control():
    pub = rospy.Publisher('fake_control_output', ControlOutput, queue_size=10)
    rospy.init_node('fake_control', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        u = ControlOutput(1.0, 0.02)
        # rospy.loginfo(u)
        pub.publish(u)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_control()
    except rospy.ROSInterruptException:
        pass
