def plot_tracks():
    ideal_track_np = np.array(ideal_track)
    ekf_track_np = np.array(ekf_track)
    plt.figure()
    plt.scatter(goal_state[0, 0], goal_state[1, 0], marker='s', s=60)
    plt.plot(ideal_track_np[:,0], ideal_track_np[:,1], color='b', lw=2)
    plt.plot(ekf_track_np[:, 0], ekf_track_np[:,1], color='r', lw=2)
    plt.axis('equal')
    plt.title("EKF Robot localization")
    plt.show()

if __name__ == '__main__':
    try:
	dt = 0.1
	start_state = array([[2.0, 2.0, 0.0]]).T
	goal_state = array([[12.0, 2.0]]).T
	init_var = [0.1, 0.1, 0.01]   # initial std for state variables x, y and theta
	std_vel = 0.1
	std_steer = 0.01
	std_range = 0.1
	std_bearing = 0.01

	ekf = RobotEKF(dt, std_vel=std_vel, std_steer=std_steer)
	ekf.x = start_state         # x, y, steer angle
	# initialize state variance P and measurement variance R
	ekf.P = np.diag([init_var[0], init_var[1], init_var[2]])
	ekf.R = np.diag([std_range**2, std_range**2, std_bearing**2])

	ideal_track = []
	ekf_track = []
	ideal_track.append(ekf.x.copy())

	pub_predict = rospy.Publisher('rover_state_predict', RoverState, queue_size=10)
	pub_update = rospy.Publisher('rover_state_update', RoverState, queue_size=10)
	rospy.init_node('EKF', anonymous=True)
	rospy.Subscriber('fake_control_output', ControlOutput, ekf_predict)
	rospy.Subscriber('fake_gps_output', RoverState, ekf_update)
	

	print('EKF initialization finished')

	rospy.spin()

	rospy.on_shutdown(plot_tracks)

    except rospy.ROSInterruptException:
        pass
