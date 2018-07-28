import sys
import random
import numpy as np
from singleton import Singleton
from node import Node
from channel import Channel
from events import Events
from log import Log
import heapq
@Singleton
class Sim:
  """
  Main Sumulator Class
  """
  def __init__(self):
    #current simulation time
    self.time = 0
    # queue of events
    self.queue = []
    # list of nodes
    self.nodes = []

  def initialize(self, nodes_position,duration,communication_range, current_seed, current_load):
    self.duration = duration
    self.channel = Channel(communication_range)
    self.nodes_position = nodes_position
    self.logger = Log('logger'+str(current_seed)+'-'+str(current_load)+'.csv') 
    self.current_load = current_load
    self.seed = current_seed
    np.random.seed(self.seed)

    for p in self.nodes_position:
      x = p[0]
      y = p[1]
      n = Node(x,y,self.channel,current_seed,current_load)
      self.nodes.append(n)
      self.channel.register_node(n)
      n.initialize()

    self.channel.update_neighbors()
    #self.channel.print_neighbors()
    for x in self.nodes:
      self.channel.get_neighbors(x)


  def get_time(self):
    return self.time

  def get_logger(self):
    return self.logger
  
  def get_current_load(self):
    return self.current_load
  
  def get_current_seed(self):
    return self.seed

  def schedule_event(self, event):
    heapq.heappush(self.queue,(event.get_event_time(),event))

  def print_initial_scheduled_events(self):
    for event in self.queue:
      print("Event %d is scheduled at time %f at Node %d" %(event[1].get_event_type(),event[1].get_event_time(),event[1].get_event_source().get_node_id()))
  
  def end_transmist_event_exist(self,source_node):
    end_tx = False
    for event in self.queue:
      if(event[1].get_event_type()!= Events.PKT_ARRIVAL):
        rules  = [event[1].get_event_type() == Events.END_TRANSMISSION,
                  event[1].get_event_source().get_node_id() == source_node.get_node_id(),
                  event[1].get_object().get_packet_id() == source_node.current_packet.get_packet_id()]
        if all(rules):
          print("Node %d is found with schdlued end_tranmist_event at %f for dst %d"%(source_node.get_node_id(),event[1].get_event_time(),event[1].get_event_destination().get_node_id()))
          end_tx = True
          break

    return end_tx
    
  def fetch_scheduled_event(self):
    try:
      event = heapq.heappop(self.queue)
      self.time = event[0]
      return event[1]
    except IndexError:
      print("No More Events Present")
      sys.exit(0)

  def run(self):
    np.random.seed(self.seed)
    while self.time <= self.duration:
      event = self.fetch_scheduled_event()
      event_type = event.get_event_type()
      event_source = event.get_event_source()
      event_dst = event.get_event_destination()
      if event_type == Events.PKT_ARRIVAL:
        node = event.get_event_source()
      elif event_type == Events.START_TRANSMISSION:
        node = event.get_event_source()
      elif event_type == Events.END_TRANSMISSION:
        node = event.get_event_source()
      elif event_type == Events.START_RECEPTION:
        node = event.get_event_destination()
      elif event_type == Events.END_RECEPTION:
        node = event.get_event_destination()
      node.handle_event(event)