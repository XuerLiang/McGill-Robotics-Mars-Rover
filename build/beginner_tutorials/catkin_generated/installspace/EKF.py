#!/usr/bin/env python2

import rospy
from beginner_tutorials.msg import ControlOutput, RoverState



class RobotEKF():
    def __init__(self):
    	self.x = 0.0
	self.y = 0.0
	self.theta = 0.0

def predict(u):
    #u = data.data
    ekf.x += u.velocity
    ekf.y += u.velocity
    ekf.theta += u.steering_angle_change
    pub.publish(RoverState(ekf.x, ekf.y, ekf.theta))
    print('EKF predict', ekf.x, ekf.y, ekf.theta)

def update(gps):
    #u = data.data
    print('from GPS ', gps.x, gps.y, gps.theta)
    ekf.x = gps.x + 1.0
    ekf.y = gps.y + 1.0
    ekf.theta = gps.theta + 0.02
    print('EKF update ', ekf.x, ekf.y, ekf.theta)


if __name__ == '__main__':
    try:
        ekf = RobotEKF()
	rospy.init_node('EKF', anonymous=True)

	rospy.Subscriber('fake_control_output', ControlOutput, predict)
	rospy.Subscriber('fake_gps_output', RoverState, update)

	pub = rospy.Publisher('rover_state', RoverState, queue_size=10)

	#rate = rospy.Rate(10) # 10hz

	#while not rospy.is_shutdown():
		
		# rospy.loginfo(u)
		
		#rate.sleep()
		# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

    except rospy.ROSInterruptException:
        pass
