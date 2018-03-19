import robot2I013

class Strat70():
    
    def __init__(robot):
        self.distance=0
        self.stop=False
        self.robot=robot
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,120)
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        
    def update():
        self.distance+=self.robot.get_motor_position()[0]
        if self.distance > 700-self.robot.WHEEL_CIRCUMFERENCE:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,60)
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        if self.distance >= 700:
            self.stop=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        
    def stop():
        return self.stop
