#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import ControlOutput, RoverState, ControlFeedbackToPlanner



def reach_goal(rover_state):
    """ check whether goal state is reached """
    #print('current state ', current_state.x, current_state.y)
    control_feedback_to_planner.rover_x = rover_state.x
    control_feedback_to_planner.rover_y = rover_state.y
    control_feedback_to_planner.rover_theta = rover_state.theta
    if abs(current_state.x - goal_state[0]) > tol or abs(current_state.y - goal_state[1]) > tol:
	pub_to_real_time_detector.publish(current_state)	
    else:
	pub_to_planner.publish(control_feedback_to_planner)

def realtime_detection(real_time_detection):
    if real_time_detection.hit:
	control_feedback_to_planner.hit_point_x = real_time_detection.x
    	control_feedback_to_planner.hit_point_y = real_time_detection.y
    	control_feedback_to_planner.hit = real_time_detection.hit
	pub_to_planner.publish(control_feedback_to_planner)
    else:
	pub_to_ekf.publish(u)
  

if __name__ == '__main__':
    try:
	goal_state = [12.0, 2.0]
	tol = .2
	u = ControlOutput(1.0, 0.02)
	control_feedback_to_planner = ControlFeedbackToPlanner(.0, .0, .0, .0, .0, False)
        
	pub_to_ekf = rospy.Publisher('fake_control_output', ControlOutput, queue_size=10)
	pub_to_planner = rospy.Publisher('control_feedback_to_planner', ControlFeedbackToPlanner, queue_size=10)
	rospy.init_node('fake_control', anonymous=True)
	rospy.Subscriber('rover_state_update', RoverState, reach_goal)
	rospy.Subscriber('real_time_detection', RealTimeDetectorOutput, realtime_detection)
	  
	pub.publish()
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
