import sim
import copy
import math
from events import Events
from event import Event
class Channel(object):
    TL = 30 
    def __init__(self,communication_range):

      self.range = communication_range
      # list of all communication nodes in the simulation
      self.nodes = []
      # hash of neighbors that maps each node id to its neighbors
      self.neighbors = {}

    def register_node(self,node):
      self.nodes.append(node)
      self.compute_neighbors(node)

    def compute_distance(self,a,b):
      return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def update_neighbors(self):
      self.neighbors.clear()
      updated_neighbors = []
      for index, n in enumerate(self.nodes):
        for index2, n2 in enumerate(self.nodes):
          if n.get_node_id() != n2.get_node_id() and self.compute_distance(n,n2) < self.range:
            updated_neighbors.append(n2)
        self.neighbors[n.node_id] =updated_neighbors
        updated_neighbors = []


    def compute_neighbors(self,new_node):
      new_node_neighbors = []
      for n in self.nodes:
        if n.get_node_id() != new_node.get_node_id() and self.compute_distance(new_node,n) < self.range:
          new_node_neighbors.append(n)

      self.neighbors[new_node.node_id] = new_node_neighbors

    def registered_nodes(self):
      for n in self.nodes:
        print ("Thr registered node info is %f %f %s and node_id is %d" %(n.x,n.y,n.state,n.node_id))

    def print_neighbors(self):
      for index, value in enumerate(self.neighbors):
        print ("Updated Neighbors of node %r is node %r." %(index,value)) 

    def neighbors_count(self,source_node):
      count = 0
      for neighbor in self.neighbors[source_node.get_node_id()]:
        count+=1
      return count
      
    def get_neighbors(self,source_node):
      for neighbor in self.neighbors[source_node.get_node_id()]:
        print ("Neighbors of node %r is node %r." %(source_node.get_node_id(),neighbor.get_node_id()))
    
    def start_transmission(self,source_node,packet):
      print ("%d Starts_Transmission:" %(source_node.get_node_id()))
      for neighbor in self.neighbors[source_node.get_node_id()]:
        estimated_propogation_delay = self.compute_distance(source_node,neighbor)/Channel.TL
        end_transmission_time = estimated_propogation_delay+sim.Sim.Instance().get_time()
        event = Event(end_transmission_time,Events.END_TRANSMISSION,source_node,neighbor,copy.deepcopy(packet))
        sim.Sim.Instance().schedule_event(event)
        sim.Sim.Instance().get_logger().schedule_end_transmission(source_node,neighbor,end_transmission_time,packet.get_packet_size())
	