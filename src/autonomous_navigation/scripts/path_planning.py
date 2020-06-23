#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import Coordinates, RoverState

from math import floor, sqrt, tan, cos, sin, atan2, asin
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def path_planning(rover_state):
    


def go_straight():
	current_coordinates = rover.x.T[0]
	angle_robot_to_goal = get_angle(current_coordinates, goal_coordinates)
	rover.x[2, 0] = angle_robot_to_goal
	next_gs_point = compute_coordinates(current_coordinates, angle_robot_to_goal, camera_max_range)
	hit = run_navigation(rover, next_gs_point, goal_coordinates, detected_obstacles_map, tol, u, ideal_track, ekf_track)

	if len(hit) == 1:
	    go_straight_mode = -1
	    break
	if len(hit) == 2:
	    visibility_point[0] = hit[0]
	    visibility_point[1] = hit[1]
	    go_straight_mode = 0
	    #print('gs_hit_obstacle ', hit)
	    break
	       
	current_coordinates = rover.x.T[0]
	print('gs_stop_point ', current_coordinates[0:2])
	current_coordinates = array([current_coordinates]).T
	gs_track.append(current_coordinates)
	frame_list.append(plt.scatter(rover.x[0, 0], rover.x[1, 0], c='green', marker='^', s=60))
	frames.append(tuple(frame_list))

def boundary_following():
        else: # boundary following
            current_coordinates = rover.x.T[0]
            # camera_angle = get_angle(current_coordinates, visibility_point)
            left_discontinuity_point, left_obst, right_discontinuity_point, right_obst = find_discontinuity_points_on_obstacle(current_coordinates, visibility_point, rover_radius, 0, camera_max_range, detected_obstacles_map)
            # print('left_and_right_points ', left_discontinuity_point, left_obst, right_discontinuity_point, right_obst)
            left_or_right = -1
            next_start_point = left_obst
            bf_point = left_discontinuity_point
            if len(left_obst) == 0 and len(right_obst) != 0:
                left_or_right = 1
                next_start_point = right_obst
                bf_point = right_discontinuity_point
            elif len(left_obst) == 0 and len(right_obst) == 0:
                left_or_right = random.choice([-1, 1])
                next_start_point = visibility_point
                bf_point = boundary_following_next_point(current_coordinates, visibility_point, left_or_right, bf_step_distance)
                print('cannot find visibility point, tangent bf point')
            elif len(left_obst) != 0 and len(right_obst) != 0:
                left_discontinuity_point_to_goal_dist = get_sq_dist(left_obst, goal_coordinates)
                right_discontinuity_point_to_goal_dist = get_sq_dist(right_obst, goal_coordinates)
                if right_discontinuity_point_to_goal_dist < left_discontinuity_point_to_goal_dist:
                    left_or_right = 1
                    next_start_point = right_obst
                    bf_point = right_discontinuity_point
                if right_discontinuity_point_to_goal_dist == left_discontinuity_point_to_goal_dist:
                    left_or_right = random.choice([-1, 1])
               
            # print('tangent point ', tangent_point_on_obstacle)
            # print('after gs discon points ', left_discontinuity_point, right_discontinuity_point)
            # print('after gs bf point ', bf_point)
            print('bf direction ', left_or_right)
            # angle_buffer = atan2(rover_radius, sqrt(get_sq_dist(current_coordinates, visibility_point)))
            # updated_angle_buffer = 0.0
            # bf_point = get_bf_point(current_coordinates, visibility_point, left_or_right, angle_buffer)
            
            while 1:
            # for i in range(2):
                print('next start point ', next_start_point)              
                bf_track.append(array([bf_point]).T)
                frame_list.append(plt.scatter(bf_point[0], bf_point[1], c='green', marker='o', s=60))
                frames.append(tuple(frame_list))

                print('bf_point ', bf_point)
                # print('position before bf ', rover.x.T[0])
                rover.x[2, 0] = get_angle(current_coordinates, bf_point)           
                hit = run_navigation(rover, bf_point, goal_coordinates, detected_obstacles_map, tol, u, ideal_track, ekf_track)
                current_coordinates = rover.x.T[0]
               
                if not path_to_goal_collision_detection(current_coordinates, goal_coordinates, detected_obstacles_map):
                    go_straight_mode = 1
                    #print('path to goal')
                    break
                if len(hit) == 1:
                    go_straight_mode == -1
                    #print('break D ', i, current_coordinates)
                    break
                elif len(hit) == 0:
                    left_discontinuity_point, left_obst, right_discontinuity_point, right_obst = find_discontinuity_points_on_obstacle(current_coordinates, next_start_point, rover_radius, left_or_right, camera_max_range, detected_obstacles_map)
                    if left_or_right == -1:
                        if len(left_obst) != 0:
                            bf_point = left_discontinuity_point
                            next_start_point = left_obst
                        else:
                            bf_point = boundary_following_next_point(current_coordinates, next_start_point, left_or_right, bf_step_distance)
                            print('cannot find visibility point, tangent bf point')
                    else:
                        if len(right_obst) != 0:
                            bf_point = right_discontinuity_point
                            next_start_point = right_obst
                        else:
                            bf_point = boundary_following_next_point(current_coordinates, next_start_point, left_or_right, bf_step_distance)
                            print('cannot find visibility point, tangent bf point')                 
                elif len(hit) == 2:
                    #print('bf_hit_obstacle ', hit)
                    print('collision detection failed: hit obstacle on way to bf point')
                    bf_point = boundary_following_next_point(current_coordinates, hit, left_or_right, bf_step_distance)
                    next_start_point = hit

if __name__ == '__main__':
    try:
	pub = rospy.Publisher('planner_output', Coordinates, queue_size=10)
	rospy.init_node('path_planner', anonymous=True)
	rospy.Subscriber('rover_state_update', RoverState, path_planning)
	

	# obstacles_dictionary = {2:{3,4}, 3:{2,3,4,5}, 4:{3,4,15}, 5:{8,9,10,14,15,16}, 6:{7,8,9,10,14,15,16,17}, 7:{6,7,14,15,16,17}, 8:{6,7,14,15,16}, 9:{7,8,9,10,15}, 
#                         10:{8,9,10}, 11:{8,9,10}, 12:{2,3,10,11}, 13:{2,3,8,9,10}, 14:{2,3,8,9}, 15:{2,3,7,8,13}, 16:{12,13,14}, 17:{11,12,13,14,15}, 18:{12,13,14,15,16},
#                         19:{13,14,15,16,17}}

	obstacles_dictionary = {2:{3,4}, 3:{2,3,4,5}, 4:{3,4,5,15}, 5:{3,4,8,9,10,14,15,16}, 6:{2,3,7,8,9,10,14,15,16,17}, 7:{2,6,7,14,15,16,17}, 8:{6,7,14,15,16}, 9:{7,8,9,10,15}, 10:{8,9,10}, 11:{8,9,10}, 12:{2,3,10,11}, 13:{2,3,8,9,10}, 14:{2,3,8,9}, 15:{2,3,7,8,13}, 16:{12,13,14}, 17:{11,12,13,14,15}, 18:{12,13,14,15,16}, 19:{13,14,15,16,17}}

	# obstacles_dictionary = {0:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 20:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 
#                         1:{0,1,10,11,20,21}, 2:{0,1,10,11,20,21}, 3:{0,1,10,11,20,21}, 4:{0,1,10,11,20,21}, 5:{5,6,15,16, 0,1,10,11,20,21}, 6:{5,6,15,16, 0,1,10,11,20,21}, 
#                         7:{5,6,15,16,0,1,10,11,20,21}, 8:{5,6,15,16,0,1,10,11,20,21}, 9:{5,6,15,16, 0,1,10,11,20,21}, 10:{5,6,15,16,0,1,10,11,20,21},11:{5,6,15,16,0,1,10,11,20,21}, 12:{5,6,15,16,0,1,10,11,20,21}, 
#                         13:{5,6,15,16,0,1,10,11,20,21}, 14:{5,6,15,16,0,1,10,11,20,21}, 15:{5,6,15,16,0,1,10,11,20,21}, 16:{5,6,15,16},17:{5,6,15,16},18:{5,6,15,16},19:{5,6,15,16}}

# obstacles_dictionary = {0:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 20:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 
#                         1:{0,1,10,11,20,21}, 2:{0,1,10,11,20,21}, 3:{0,1,10,11,20,21}, 4:{0,1,10,11,20,21}, 5:{5,6, 0,1,10,11,20,21}, 6:{5,6, 0,1,10,11,20,21}, 
#                         7:{5,6,0,1,10,11,20,21}, 8:{5,6,0,1,10,11,20,21}, 9:{5,6, 0,1,10,11,20,21}, 10:{5,6,0,1,10,11,20,21},11:{5,6,0,1,10,11,20,21}, 12:{5,6,0,1,10,11,20,21}, 
#                         13:{5,6,0,1,10,11,20,21}, 14:{5,6,0,1,10,11,20,21}, 15:{5,6,0,1,10,11,20,21}, 16:{5,6},17:{5,6},18:{5,6},19:{5,6}}

# obstacles_dictionary = {0:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 20:{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}, 
#                         1:{0,1,10,11,20,21}, 2:{0,1,10,11,20,21}, 3:{0,1,10,11,20,21}, 4:{0,1,10,11,20,21}, 5:{5,6,15,16, 0,1,10,11,20,21}, 6:{5,6,15,16, 0,1,10,11,20,21}, 
#                         7:{5,6,15,16,0,1,10,11,20,21}, 8:{5,6,15,16,0,1,10,11,20,21}, 9:{5,6,15,16, 0,1,10,11,20,21}, 10:{5,6,15,16,0,1,10,11,20,21},11:{5,6,15,16,0,1,10,11,20,21}, 12:{5,6,15,16,0,1,10,11,20,21}, 
#                         13:{5,6,15,16,0,1,10,11,20,21}, 14:{5,6,15,16,0,1,10,11,20,21}, 15:{5,6,15,16,0,1,10,11,20,21}, 16:{5,6,15,16,20,21},17:{5,6,15,16,20,21},18:{5,6,15,16,20,21},19:{5,6,15,16,20,21}}

	obstacles_temp = []
	for i in obstacles_dictionary:
	    for j in obstacles_dictionary[i]:
		obstacles_temp.append([i, j])
	obstacles = np.array(obstacles_temp)

	frames = []
	frame_list = []

	dt = 0.1

	start_state = array([[12.0, 9.0, 0.0]]).T
	goal_state = array([[7.0, 8.0]]).T
	tol = .2
	u = ControlOutput(1.0, 0.02)
        
	std_vel = 0.1
	std_steer = 0.01
	std_range=0.1
	std_bearing=0.01

	goal_coordinates = goal_state.T[0]
	init_var = [0.1, 0.1, 0.01]   # initial std for state variables x, y and theta

	start = start_state.T
	goal = goal_state.T

	fig = plt.figure(figsize=(8.,6.))
	frame_list.append(plt.scatter(obstacles[:, 0], obstacles[:, 1], c='black', marker='s', s=90))
	frames.append(tuple(frame_list))
	frame_list.append(plt.scatter(start[0, 0], start[0, 1], c='red', marker='o', s=60))
	frames.append(tuple(frame_list))
	frame_list.append(plt.scatter(goal[0, 0], goal[0, 1], c='blue', marker='o', s=60))
	frames.append(tuple(frame_list))


	#rover = RobotEKF(dt, std_vel=std_vel, std_steer=std_steer, init_var=init_var, std_range=std_range, std_bearing=std_bearing)
	#rover.x = start_state         # x, y, steer angle

	camera_max_range = 5.0
	rover_radius = 0.5
	tol = 0.3

	bf_step_distance = 1.0
	u = [1.0, 0.0]

	gs_track = []
	bf_track = []
	ideal_track = []
	ekf_track = []


	current_coordinates = rover.x.T[0]
	angle_robot_to_goal = get_angle(current_coordinates, goal_coordinates)

	go_straight_mode = 1

	detected_obstacles_map = {}
	visibility_point = [0.0, 0.0]

	pub.publish()

	rospy.spin()
    except rospy.ROSInterruptException:
        pass
