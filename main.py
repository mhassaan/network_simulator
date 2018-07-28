import sim
import math
import numpy as np
from result_main import ResultMain
import matplotlib.pyplot as plt
# positioning of nodes
nodes_position =[(0.163, 0.008), (0.372, 0.491), (0.452, 0.108),(0.997, 0.344),(0.838, 0.155),(0.345, 0.324),(0.643, 0.062),(0.338, 0.437),(0.501, 0.58),(0.245, 0.015)]
# duration of simulation in seconds
duration = 100
# range of communication in meters
communication_range = 0.25
seeds = [0,1,2,3,4,5,6,7,8,9]
# Seeds 
# Load on Network
#offered_load  = [10,60,110,160,210,260,360,410,460,510,1510]
offered_load  = [10,210,510,1510]
#Initialzing Simulator
simulator = sim.Sim.Instance()
simulator.initialize(nodes_position,duration,communication_range,seeds[0],offered_load[0]) 
simulator.run()
