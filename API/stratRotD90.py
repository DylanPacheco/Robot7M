import robot2I013

class StratRotD90():
    
    def __init__(robot):
        self.rot=0
        self.stop=False
        self.robot=robot
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-10)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,10)
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        
    def update():
        self.rot+=self.robot.get_motor_position()[0]
        if self.rot >= 90:
            self.stop=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        if self.rot >= 75:
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-5)
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,5)
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        
    def stop():
        return self.stop
