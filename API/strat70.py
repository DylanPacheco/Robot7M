import robot2I013

class Strat70():
    
    def __init__(robot):
        self.distance=0
        self.stop=False
        self.robot=robot
        self.robot.set_motor_dps(MOTOR_LEFT+MOTOR_RIGHT,120)
        
    def update():
        self.distance+=get_motor_position()[0]
        if distance >= 700:
            stop=True
        if distance < 700-WHEEL_CIRCUMFERENCE:
            self.robot.set_motor_dps(MOTOR_LEFT+MOTOR_RIGHT,60)
        
    def stop():
        return stop
