from robot2I013 import *
import math

class StratRond():
    
    def __init__(robot, rayon):
        self.distance=0
        self.stop=False
        self.robot=robot
        self.rayon=rayon
        self.coeff=(rayon-WHEEL_BASE_WIDTH/2)/(rayon+WHEEL_BASE_WIDTH/2)
        self.robot.set_motor_dps(robot.MOTOR_LEFT,120)
        self.robot.set_motor_dps(robot.MOTOR_RIGHT,120*coeff)
        
    def update():
        
            
    def stop():
        return self.stop
