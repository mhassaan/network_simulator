from result import Result
from plot_result import PlotResult
class ResultMain:
  def __init__(self,duration):
    self.result = Result(duration)
    self.plot_result = PlotResult(duration)
  
  # Print average results for loss rate.
  def avg_loss_rate(self,load):
    avg_lr = self.result.average_loss_rate(load)
    print("Average Loss rate at load %d is" %(load))
    print(avg_lr)
  
  # Print average results for collision rate.
  def avg_collision_rate(self,load):
    avg_cr = self.result.average_collision_rate(load)
    print("Average Collision rate at load %d is" %(load))
    print(avg_cr)    
  
  # Print average results for throughput rate.
  def average_throughput_by_node(self,load):
    avg_tp = self.result.average_throughput_by_node(load)
    print("Average Throughput at load %d is" %(load))
    print(avg_tp)
  
  # Plotting collision rate at every node.
  def plot_collision_rate(self,load):
    self.plot_result.plot_collision_rate(load)

  # Plotting loss rate at every node.
  def plot_loss_rate(self,load):
    self.plot_result.plot_loss_rate(load)

# Plotting throughput at every node.
  def plot_throughput(self,load):
    self.plot_result.plot_throughput(load)

# Plotting throughput by load 
  def plot_throughput_by_load(self):
    self.plot_result.plot_throughput_by_load()

# Plotting nodes on axis.
  def plot_nodes_on_axis(self):
    self.plot_result.plot_nodes_on_axis()