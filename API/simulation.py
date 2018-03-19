import stratCarre70

class Simulation():

	def __init__(robot):
		self.strategie = StratCarre70(robot)

	def run(self):
		cpt=0
		while not self.strategie.stop():
			self.strategie.update()
			cpt+=1
		print("Stoping")
