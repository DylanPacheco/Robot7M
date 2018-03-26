
import math
import robot
import robot2I013
import simulation
#code

class Translate:

"""Partie Robot Virtuel"""

    def __init__(self, position, coords, direction, dimension, vitesse, r=robot.Robot(position, coords, direction, dimension, vitesse, strat), strat=simulation.Simulation(r)):
        self.r=r
        self.strat=strat
        self.r1v=vitesse
        self.r2v=vitesse

    def move_bis(self):
        self.r.move_bis()
        
    def interprete_strat(self, s):
        self.strat.run()
    	   
    def retourne_angle(self,x,y,xx,yy) :
        self.r.retourne_angle(x,y,xx,yy)
       
    def rotation_bis(self,teta):
        self.r.rotation_bis(teta)
         
    def calcdir(self):
        return self.r.calcdir()
    
    def rotation_tete(self, teta):
        return self.r.rotation_tete(teta)

    def toString(self):
        return "ROBOT[Corps]|position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())+"\n"+self.tete.toString()

    def safficher(self):
                """Methode d'affichage d'un robot au format :
                Robot[position, direction, taille, vitesse]
                """
                return "ROBOT([Corps] position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())#||| "+self.tete.safficher()+")"
                
              
    """-----------------------GETTTER-------------------------"""
    def getPosition(self):
        return self.r.position

    def getDirection(self):
        return self.r.direction

    def getDimension(self):
        return self.r.dimension

    def getVitesse(self):
        return self.r.vitesse

    """-----------------------SETTER-------------------------"""
    def __setPosition(self, position):
        self.r.position = position

    def __setDirection(self, direction):
        self.r.direction = direction

    def setVitesse(self, vitesse):
        self.r.vitesse = vitesse

    def setCoords(self, coords):
        self.r.coords = coords
        
    def setStrat(self, strat):
        self.r.strat= strat
        
    """-----------------------SAVER-------------------------"""
    def toSaveF(self, f):
        """Ecrit les coordonnees du robot dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Robot;' + str(self.position) + ';' +  str(self.direction) + ';' + str(self.dimension) + ';' + str(self.vitesse) + ';\n')
        
def Creation_Robot(arene):

"""Partie robot reel"""

    def set_motor_dps(self, port, dps):
        if(port==3):  
            self.r.setVitesse(dps/360*robot2I013.WHEEL_DIAMETER)
            self.r.move()
        else
    
    def set_motor_limits(self,port,dps):
    
    def get_motor_position(self):

    def set_motor_position(self, port, position):
    
    def offset_motor_encoder(self, port, offset):
    
    def get_distance(self):
    
    def servo_rotate(self,position):
    
    def stop(self):
        self.setVitesse(0)
