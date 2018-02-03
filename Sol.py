from Cube import *
from Arene import *

class Sol(Cube):
    """Classe héritant de la classe Cube, caractérisée par:
        -ses coordonnées: x, y, z
        -sa hauteur
        -sa largueur
        -sa longueur"""

    def __init__(self, x, y, z, larg, long):
        """Constructeur de la classe Cube"""
        Cube.__init__(self,x,y,z,larg,long,1)

    def safficher(self):
        """Methode d'affichage d'un sol au format :
        sol[x= , y= , z= , larg= , long= , haut= ]
        """
        print("Sol(x=%.2f,y=%.2f,z=%.2f, larg=%.2f,long=%.2f,haut=%.2f)"%(self.x, self.y, self.z, self.larg, self.long, self.haut))


def Creation_Sol(arene): #parametre obligatoire pour pouvoir recupérer les dimensions de l'arene
    """Création d'un sol avec une hauteur = 1 et une taille (larg, long) par les limites de l'Arene"""
    x = 0
    y = 0
    z = 0

    larg = arene.lx
    long = arene.ly

    return Sol(x, y, z, larg, long)
