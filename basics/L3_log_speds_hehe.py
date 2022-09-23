import L1_log as log
import L1_ina as botData
import L2_kinematics as kin
import L2_speed_control as sc
import L1_encoder as enc
import numpy as np
from time import sleep


while(1):
    wheelSped = kin.getPdCurrent()
    log.tmpFile(wheelSped[0], "PDL")
    log.tmpFile(wheelSped[1], "PDR")
    
    botSpeds = kin.getMotion()
    log.tmpFile(botSpeds[0], "xdot")
    log.tmpFile(botSpeds[1], "thetadot")
    
    botVolt = botData.readVolts()
    log.tmpFile(botVolt, "voltage")

    print("Forard Velocity: ", botSpeds[0], "m/s | Angular Velocity: ", botSpeds[1], "rads/s | PDL: ", wheelSped[0], "rads/s | PDR: ", wheelSped[1], "rads/s")
    sleep(1)

