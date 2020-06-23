#!/usr/bin/env python2

import rospy
from beginner_tutorials.msg import ControlOutput, RoverState

from filterpy.kalman import ExtendedKalmanFilter as EKF
import numpy as np
from numpy import dot, array, sqrt
from numpy.random import randn
from math import atan2, sqrt
import sympy
from sympy import symbols, Matrix
from sympy.abc import beta, x, y, v, R, theta
from math import sqrt, tan, cos, sin, atan2
import matplotlib.pyplot as plt



class RobotEKF(EKF):
    def __init__(self, dt, std_vel, std_steer):
        EKF.__init__(self, 3, 2, 2)
        self.dt = dt
        self.std_vel = std_vel
        self.std_steer = std_steer

        beta, x, y, v, theta, time = symbols(
            'beta, x, y, v, theta, t')
        d = v*time
    
        self.fxu = Matrix([[x + d*sympy.sin(theta+beta)],
                           [y + d*sympy.cos(theta+beta)],
                           [theta+beta]])

        self.F_j = self.fxu.jacobian(Matrix([x, y, theta]))
        self.V_j = self.fxu.jacobian(Matrix([v, beta]))

        # save dictionary and its variables for later use
        self.subs = {x: 0, y: 0, v:0, beta:0, 
                     time:dt, theta:0}
        self.x_x, self.x_y, = x, y 
        self.v, self.beta, self.theta = v, beta, theta

    def predict(self, control_output):
	u = array([control_output.velocity, control_output.steering_angle_change])
        self.x = self.move(self.x, u, self.dt)
        self.subs[self.theta] = self.x[2, 0]
        self.subs[self.v] = u[0]
        self.subs[self.beta] = u[1]

        F = array(self.F_j.evalf(subs=self.subs)).astype(float)
        V = array(self.V_j.evalf(subs=self.subs)).astype(float)

        # covariance of motion noise in control space
        M = array([[self.std_vel**2, 0], 
                   [0, self.std_steer**2]])

        self.P = dot(F, self.P).dot(F.T) + dot(V, M).dot(V.T)
	# publish
	x, y, theta = self.x[0, 0], self.x[1, 0], self.x[2, 0]
	print('ekf predict ', x, y)
	pub_predict.publish(RoverState(x, y, theta))
	

    def move(self, x, u, dt):
        theta = x[2, 0]
        vel = u[0]
        beta = u[1]
        dist = vel * dt
        new_theta = (theta + beta) % (2 * np.pi)
        if new_theta > np.pi:             # move to [-pi, pi)
            new_theta -= 2 * np.pi

        new_x = np.array([[x[0, 0] + dist*sin(new_theta)], 
                          [x[1, 0] + dist*cos(new_theta)], 
                          [new_theta]])
        return new_x

def H_of(x):
    """ compute Jacobian of H matrix where h(x) computes 
    the range and bearing to a landmark for state x """
    H = array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1],])
    
    return H

def Hx(x):
    """ takes a state variable and returns the measurement
    that would correspond to that state. """
    Hx = array([[x[0, 0]],
                [x[1, 0]],
                [x[2, 0]]])
    
    return Hx

def residual(a, b):
    """ compute residual (a-b) between computed measurement and 
    machine measurement containing [range, bearing]. 
    Bearing is normalized to [-pi, pi)"""
    y = a - b
    y[2] = y[2] % (2 * np.pi)    # force in range [0, 2 pi)
    if y[2] > np.pi:             # move to [-pi, pi)
        y[2] -= 2 * np.pi
    return y

def ekf_predict(control_output):
    print('here')
    ekf.predict(control_output)

def ekf_update(gps):
    z = np.array([[gps.x], [gps.y], [gps.theta]])
    ekf.update(z, HJacobian=H_of, Hx=Hx, residual=residual)
    x, y, theta = ekf.x[0, 0], ekf.x[1, 0], ekf.x[2, 0]
    print('ekf update ', x, y)
    pub_update.publish(RoverState(x, y, theta))


if __name__ == '__main__':
    try:
	dt = 0.1
	start_state = array([[2.0, 2.0, 0.0]]).T
	
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

	#ideal_state = ekf.x.copy() # simulated position
	#ideal_track = []
	#ekf_track = []

	rospy.init_node('EKF', anonymous=True)
	rospy.Subscriber('fake_control_output', ControlOutput, ekf_predict)
	rospy.Subscriber('fake_gps_output', RoverState, ekf_update)
	pub_predict = rospy.Publisher('rover_state_predict', RoverState, queue_size=10)
	pub_update = rospy.Publisher('rover_state_update', RoverState, queue_size=10)

	print('EKF initialization finished')

	rospy.spin()

    except rospy.ROSInterruptException:
        pass
