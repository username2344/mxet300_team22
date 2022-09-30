import L1_lidar as ldr
import L1_log as log
import L2_vector as vect
from time import sleep

while (1):
    heading = vect.getNearest()
    log.tmpFile(heading[1], "heading")
    log.tmpFile(heading[0], "distance")
    
    
    
    cart = vect.polar2cart(heading[0], heading[1])
    log.tmpFile(cart[0], "x_axis")
    log.tmpFile(cart[1], "y_axis")
    
    print(heading[1], "heading", heading[0], "distance", cart[0], "x axis", cart[1], "y axis")
    sleep(1)