# this code is intended to be used to create a path utilising inverse kinematics
# use this code as a template to create pre-determined paths using known chassis forward velocity (x dot) in m/s, 
# chassis angular velocity (theta dot) in rad/s, and motion duration in sec for each motion to create the path

import L1_log as log
import L2_inverse_kinematics as ik
import L2_speed_control as sc
import numpy as np
from time import sleep

#t-22: these are the team-determined segment lengths and forward velocity for the SCUTTLE to follow to complete the s-shaped path.
#t-22: these variables are not used in the following script but were used by the team to determine the ideal xdot (column 0 in motions) to be sent to the SCUTTLE.
pi = np.pi
d1 = 1.2
d2 = 1.6
forward_velocity = 0.4

#t-22: motions is the array being used to give seperate directions for SCUTTLE to follow, each row is taken into the for loop below.
#t-22: Column 0 is the xdot, column 1 is thetadot, and column 2 is duration
motions = [
    [0.4, 0.0, 3.0],            # Motion 1
    [0.0, 1.5, 1.0],            # Motion 2
    [0.4, 0.0, 4.0],            # Motion 3
    [0.0, 1.5, 1.0],            # Motion 4
    [0.4, 0.0, 3.0],            # Motion 5            
    [0.0, -1.5, 1.0],           # Motion 6           
    [0.4, 0.0, 4.0],            # Motion 7
    [0.0, -1.5, 1.0],           # Motion 8
    [0.4, 0.0, 3.0],            # Motion 9
    [0.0, 0.0, 0.0],            # Motion 10
]

for  count, motion in enumerate(motions): #T-22: following steps repeats for each row in the motions array
    print("Motion: ", count+1, "\t Chassis Forward Velocity (m/s): {:.2f} \t Chassis Angular Velocity (rad/s): {:.2f} \t Duration (sec): {:.2f}".format(motion[0], motion[1], motion[2]))
    wheel_speeds = ik.getPdTargets(motion[:2])                  # t-22: converts the first 2 values in each row (xdot and thetatdot) to left and right wheel speeds
    sc.driveOpenLoop(wheel_speeds)                              # t-22: converts target wheel speeds to PWM, splits them up and sends pdl to left wheel and pdr to the right wheel
    sleep(motion[2])                                            # t-22: sleeps while driving instructions are being carried out for desired time from 3rd value in each row
        
#Code for post lab question 3:        
#    botSpeed = str(robotSpeedTarget[0])
#    botDir = str(robotSpeedTarget[1])
#    nodeWrite.tmpFile(botSpeed, "Speed")
#    nodeWrite.tmpFile(botSpeed, "Direction")
    
    
