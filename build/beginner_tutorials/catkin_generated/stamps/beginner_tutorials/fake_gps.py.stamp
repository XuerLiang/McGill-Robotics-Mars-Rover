#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import RoverState

x = 0.0
y = 0.0
theta = 0.0

def get_measurement(ekf_predict):
    x = ekf_predict.x + 1.0
    y = ekf_predict.y + 1.0
    theta = ekf_predict.theta + 0.02
    print('gps_output ', x, y, theta)
    pub.publish(RoverState(x, y, theta))


if __name__ == '__main__':
    try:
        rospy.init_node('fake_gps', anonymous=True)
	pub = rospy.Publisher('fake_gps_output', RoverState, queue_size=10)
	rospy.Subscriber('rover_state', RoverState, get_measurement)
	
	#rate = rospy.Rate(10) # 10hz
	#while not rospy.is_shutdown():
	#gps_output = RoverState(x, y, theta)
	#rate.sleep()
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
