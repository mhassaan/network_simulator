# Analysis of a wireless network.
This programs simulates a small network comprised of ten stations under some simple network protocls.
### Requirements
- Python 3.5.2
- Matplotlib 
- Networkx

### Usage
In the program's file i.e. main.py, you can configure the values for following variables,

- Duration(total period of simulation)
- Seeds(starting value that is used to generate numbers randomly during the whole process of simulation)
- Offered Load(Value that controls the interarrival time of packets.)

You have to set these values manually before every run of the simulation.
```
seeds = [0,1,2,3,4,5,6,7,8,9]
offered_load = [10,210,510,1510]
simulator.initialize(nodes_position,duration,communication_range,seeds[0],offered_load[0]) 
```
So by running the simulation at load 10 for each of the seed values, one will get 10 different files.These files will then be used to generate average results for throughput, loss rate and collision rate at load 10 for different seed values.

### Generating Reults
After generating data files for different loads at all seed values, one would have to generate results.For producing results, one would have to use result_main.py. 
### Usage 
```
rm = ResultMain(duration)
# Plotting loss rate at every node for a particular load.
rm.plot_loss_rate(load)
# Plotting collison rate at every node for a particular load.
rm.plot_collision_rate(load)
# Plotting throughput at every node for a particular load.
rm.plot_throughput(load)
```

In order to save time of running simulation at a particular load for every seed value, i have attached a zip file name sample_data.zip inside the project's  folder, you can unzip it and verify the results attached with the report.