#!/usr/bin/env python

import rospy
from numpy.random import randn
from beginner_tutorials.msg import RoverState
from numpy import pi

def get_measurement(ekf_predict):
    """ simulate measurement by adding random noise within variance range """ 
    noised_theta = (ekf_predict.theta + randn()*std_brg) % (2 * pi)
    if noised_theta > pi:  # move to [-pi, pi)
        noised_theta -= 2 * pi
    #print('GPS output')
    pub.publish(RoverState(ekf_predict.x + randn()*std_rng, ekf_predict.y + randn()*std_rng, noised_theta))


if __name__ == '__main__':
    try:
	std_rng = 0.1
	std_brg = 0.01
        rospy.init_node('fake_gps', anonymous=True)
	pub = rospy.Publisher('fake_gps_output', RoverState, queue_size=10)
	rospy.Subscriber('rover_state_predict', RoverState, get_measurement)
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
