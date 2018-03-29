import strat70
import stratRotD90
import stratCarre70
import robot2I013
import simulation

robot=robot2I013.Robot2I013()

#strat=strat70.Strat70(robot)
strat=stratCarre70.StratCarre70(robot)
#strat=stratRotD90.StratRotD90(robot)

simul=simulation.Simulation(strat)
simul.run()
