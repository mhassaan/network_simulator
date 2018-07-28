from result import Result
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
class PlotResult:
  
  def __init__(self,duration):
    self.result = Result(duration)
    self.labels = ['N1', 'N2', 'N3','N4','N5','N6','N7','N8','N9','N10']
    self.colors = ['pink', 'lightblue', 'lightgreen', 'cyan','pink', 'lightblue', 'lightgreen', 'cyan','pink', 'lightblue']
    self.fig, self.axes = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))
  
  def plot_nodes_on_axis(self):
    pos = {1: (0.163, 0.008), 2: (0.372, 0.491), 3: (0.452, 0.108), 4: (0.997, 0.344),5: (0.838, 0.155),6: (0.345, 0.324),7: (0.643, 0.062),8: (0.338, 0.437),9: (0.501, 0.58),10: (0.245, 0.015)} 
    graph = nx.Graph()
    graph.add_nodes_from(pos.keys())
    graph.add_edges_from([(1, 10), (2, 6),(2, 8),(2, 9),(3, 6),(3, 7),(3, 10),(4, 5),(5, 7),(6, 8),(8, 9)])
    nx.draw(graph,pos, with_labels= True)
    plt.show()
  
  def plot_collision_rate(self,load):
    rate = {}
    data = []
    for node in range(1,11):
      collision_rate = self.result.collision_rate_by_node(node,load)
      rate[node]=collision_rate
    
    for items in sorted(rate):
      data.append(rate[items])
      
    bplot = self.axes.boxplot(data,
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=self.labels) 
    self.axes.set_title(label='Collision Rate For Load {}'.format(load))
    self.axes.set_xlabel('Nodes')
    self.axes.set_ylabel('Collision Rate i.e. # of pkts rcvd + # of pkts crptd/ Total Duration')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
      plt.setp(bplot[element], color='blue')

    for patch,color in zip(bplot['boxes'],self.colors):
      patch.set(facecolor=color)    
    plt.show()
  
  def plot_loss_rate(self,load):
    rate = {}
    data = []
    for node in range(1,11):
      loss_rate = self.result.loss_rate_by_node(node,load)
      rate[node]=loss_rate
    
    for items in sorted(rate):
      data.append(rate[items])

    bplot = self.axes.boxplot(data,
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=self.labels) 
    self.axes.set_title('Loss Rate For Load Load {}'.format(load))
    self.axes.set_xlabel('Nodes')
    self.axes.set_ylabel('Loss Rate i.e. # of packets lost/ # of packets sent')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
      plt.setp(bplot[element], color='blue')

    for patch,color in zip(bplot['boxes'],self.colors):
      patch.set(facecolor=color)    
    plt.show()

  def plot_throughput(self,load):
    thrpt = {}
    data = []
    for node in range(1,11):
      tp = self.result.throughput_by_node(node,load)
      thrpt[node]=tp

    for items in sorted(thrpt):
      data.append(thrpt[items])
    print ("Througput at Load {}".format(load))
    print(data)
    bplot = self.axes.boxplot(data,
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=self.labels) 
    self.axes.set_title('Throughput For Load Load {}'.format(load))
    self.axes.set_xlabel('Nodes')
    self.axes.set_ylabel('Throughput i.e. total bits received / simulation time')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
      plt.setp(bplot[element], color='blue')

    for patch,color in zip(bplot['boxes'],self.colors):
      patch.set(facecolor=color)    
    plt.show()

  def plot_throughput_by_load(self):
    plt.style.use('fivethirtyeight')
    res = self.result.throughput_by_load()
    x = [10,210,510,1510]
    #fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))
    self.axes.plot(x, res)
    plt.show()
