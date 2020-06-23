#!/usr/bin/env python

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

    def predict(self, u=0):	
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
    u = array([control_output.velocity, control_output.steering_angle_change])
    # ideal movement of robot
    new_ideal_state = ekf.move(ideal_track[-1], u, dt)
    #print('new ideal state ', new_ideal_state)
    # keep track of the ideal path 
    ideal_track.append(new_ideal_state)

    # apply noise to control with EKF
    ekf.predict(u=u)
    # publish
    x, y, theta = ekf.x[0, 0], ekf.x[1, 0], ekf.x[2, 0]
    print('ekf predict ', x, y)
    pub_predict.publish(RoverState(x, y, theta))

def ekf_update(gps):
    z = np.array([[gps.x], [gps.y], [gps.theta]])
    ekf.update(z, HJacobian=H_of, Hx=Hx, residual=residual)
    # keep track of the EKF path
    ekf_track.append(ekf.x)
    x, y, theta = ekf.x[0, 0], ekf.x[1, 0], ekf.x[2, 0]
    print('ekf update ', x, y)
    pub_update.publish(RoverState(x, y, theta))


