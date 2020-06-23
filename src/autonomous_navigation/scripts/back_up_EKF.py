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


def get_measurement(ekf_predict):
    x = ekf_predict.x + 1.0
    y = ekf_predict.y + 1.0
    theta = ekf_predict.theta + 0.02
    print('gps_output ', x, y, theta)
    pub.publish(RoverState(x, y, theta))

def run_navigation(start_state, goal_state, init_var, tol, std_vel, std_steer, 
                     std_range, std_bearing,
                     step=10, ellipse_step=50, ylim=None):
    

    # simulated movement, i.e. half circle
    while not reach_goal(ekf.x, goal_state, tol=tol):
        # get control
        u = array([1.0, .02])  # steering command (vel, steering angle change)
        # u = get_control(current_state, goal_state)

        # ideal movement of robot
        ideal_state = ekf.move(ideal_state, u, dt)
        # keep track of the ideal path
        ideal_track.append(ideal_state)

        # apply noise to control and measurement with EKF
        ekf.predict(u=u)
	x, y, theta = ekf.x[0, 0], ekf.x[1, 0], ekf.x[2, 0]
	pub.publish(RoverState(x, y, theta))
        
        ekf.update(z, HJacobian=H_of, Hx=Hx, residual=residual)
        # keep track of the EKF path
        ekf_track.append(ekf.x)

    ideal_track = np.array(ideal_track)
    ekf_track = np.array(ekf_track)

    plt.figure()
    plt.scatter(goal_state[0, 0], goal_state[1, 0], marker='s', s=60)
    plt.plot(ideal_track[:,0], ideal_track[:,1], color='b', lw=2)
    plt.plot(ekf_track[:, 0], ekf_track[:,1], color='r', lw=2)
    plt.axis('equal')
    plt.title("EKF Robot localization")
    if ylim is not None: plt.ylim(*ylim)
    plt.show()
    return ekf



