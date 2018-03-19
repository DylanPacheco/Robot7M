import strat70
import robot2I013

class StratCarre70():
    
    def __init__(robot):
        self.distance=0
        self.cpt=0
        self.stop=False
        self.robot=robot
        self.S70=Strat70(robot)
        
    def update():
        while cpt < 4:
            while not self.S70.stop():
                self.S70.update()
            self.robot.set_motor_position(MOTOR_RIGHT,-90)
            self.robot.set_motor_position(MOTOR_LEFT,90)
            cpt+=1
        self.stop=True
            
    def stop():
        return stop
