class Strat:

    def __init__(self, id, listeParam=[]):
        self.id = id
        self.Lstrat = self.listStrat(id, listeParam)
		
    def listStrat(self, id, listeParam=[10, 'R']):
        Lstrat = []
        if(id==1):
            print("Strategie <Carré> initialisée")
            for i in range(listeParam[0]):
                Lstrat.append('F')
            Lstrat.append(listeParam[1])
            Lstrat=Lstrat*4
        elif(id==2):
            print("Strategie <ToutDroit> initialisée")
            for i in range(listeParam[0]):
                Lstrat.append('F')
        return Lstrat		
			
			
