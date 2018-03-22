import strat70
import stratRotD90
import stratCarre70
import robot2I013
import simulation

robot=robot2I013.Robot2I013()
strat=stratCarre70.StratCarre70(robot)
simul=simulation.Simulation(strat)
simul.run()
