import random
import numpy as np
from events import Events
from event import Event
from collections import deque 
from packet import Packet
from channel import Channel
import sim 

class Node(object):
	# list of possible states
	IDLE = 0
	SENDING = 1
	RECEIVING = 2
	TRANSMISSION_RATE = 8000000
	__nodes_count = 1
	# Node Buffer Size
	QUEUE = 20
	# Max Packet Size
	MAX_SIZE = 4645
	MIN_SIZE = 32

	def __init__(self,x,y,channel,current_seed,current_load):
		# buffer of packets, using list as a queue
		self.queue = deque()
		self.x = x
		self.y = y
		self.node_id = Node.__nodes_count
		self.state = Node.IDLE
		self.queue_size = Node.QUEUE
		self.max_size = Node.MAX_SIZE
		self.min_size = Node.MIN_SIZE
		self.channel = channel
		self.current_packet = None
		Node.__nodes_count = Node.__nodes_count + 1


	def get_node_id(self):
		return self.node_id

	def initialize(self):
		self.schedule_next_arrival()
    
	def schedule_next_arrival(self):
		current_load = sim.Sim.Instance().get_current_load()
		inter_arrival = np.random.exponential(1/current_load)
		simulation_time = sim.Sim.Instance().get_time()
		print("Interarrival time inside schedule arrival is %f" %(inter_arrival))
		print("Next Interarrival time inside schedule arrival is %f" %(inter_arrival+simulation_time))
		event = Event(inter_arrival+simulation_time,Events.PKT_ARRIVAL,self,self)
		sim.Sim.Instance().schedule_event(event)


	def handle_event(self,event):
		if event.get_event_type() == Events.START_TRANSMISSION:
			self.start_transmission()
		elif event.get_event_type() == Events.END_TRANSMISSION:
			self.handle_end_transmission(event)
		elif event.get_event_type() == Events.START_RECEPTION:
			self.handle_start_reception(event)
		elif event.get_event_type() == Events.END_RECEPTION:
			self.handle_end_reception(event)
		elif event.get_event_type() == Events.PKT_ARRIVAL:
			self.handle_packet_arrival(event)
	
	def handle_packet_arrival(self,event):
		packet_size = np.random.geometric(p=0.019)
		sim.Sim.Instance().get_logger().log_packet_arrival(self,packet_size)
		if self.state == Node.IDLE:
			if len(self.queue) > 0:
				packet_size = self.queue.popleft()
			self.start_transmission(packet_size)
		else:
			if len(self.queue) < self.queue_size:
				self.queue.append(packet_size)
			else:
				sim.Sim.Instance().get_logger().log_packet_drop(self,packet_size)
		self.schedule_next_arrival()

	def start_transmission(self,packet_size):
		duration = packet_size*8/Node.TRANSMISSION_RATE
		packet = Packet(packet_size,duration)
		if (self.min_size <= packet_size <= self.max_size):
			self.state = Node.SENDING
			self.current_packet = packet
			sim.Sim.Instance().get_logger().schedule_start_transmission(self,sim.Sim.Instance().get_time(),packet_size)			
			self.channel.start_transmission(self,packet)
		else:
			self.state = Node.IDLE
			self.current_packet = packet
			self.current_packet.set_state(Packet.PKT_CORRUPTED)
			sim.Sim.Instance().get_logger().log_packet_state(self,'PKT_CRPTD',packet_size)

	def handle_end_transmission(self,event):
		end_tx_rules = [self.state == Node.SENDING,
						self.current_packet is not None,
						self.current_packet.get_packet_id() == event.obj.get_packet_id()
						]
		transmitted_pkt = event.obj.get_packet_size()
		src_node = event.get_event_source()
		dst_node = event.get_event_destination()
		start_reception_time = event.obj.duration+sim.Sim.Instance().get_time()
		if all(end_tx_rules):
			if sim.Sim.Instance().end_transmist_event_exist(src_node):
				print("In handle_end_transmission event Node state is %d" %(src_node.state))
			else:
				print("In handle_end_transmission event Node state has been set to IDLE")
				src_node.state = Node.IDLE

			event = Event(start_reception_time,Events.START_RECEPTION,src_node,dst_node,event.get_object())
			sim.Sim.Instance().schedule_event(event)
			sim.Sim.Instance().get_logger().schedule_start_reception(dst_node,start_reception_time,transmitted_pkt)
		else:
			print ("Something's went wrong!")
	
	def handle_start_reception(self,event):
		pkt = event.obj
		packet_size = pkt.get_packet_size()
		reciever_node = event.get_event_destination()
		source_node = event.get_event_source()
		proc_time = 0.000003
		if reciever_node.state == Node.IDLE:
			reciever_node.state = Node.RECEIVING
			sim.Sim.Instance().get_logger().log_start_reception(self,packet_size)
			end_reception_time = sim.Sim.Instance().get_time()+proc_time
			handle_end_reception = Event(end_reception_time,Events.END_RECEPTION, self,reciever_node,pkt)
			sim.Sim.Instance().schedule_event(handle_end_reception)
		else:
			reciever_node.current_packet.set_state(Packet.PKT_CORRUPTED)
			sim.Sim.Instance().get_logger().log_packet_loss(reciever_node,packet_size)
			sim.Sim.Instance().get_logger().log_packet_state(self,'PKT_CRPTD',packet_size)

	def handle_end_reception(self,event):
		pkt = event.obj
		packet_size = pkt.get_packet_size()
		sim.Sim.Instance().get_logger().log_end_reception(self,packet_size)
		if self.state == Node.RECEIVING:
			self.state = Node.IDLE
			sim.Sim.Instance().get_logger().log_packet_state(self,'PKT_RCVD',packet_size)
		else:	
			sim.Sim.Instance().get_logger().log_packet_loss(self,packet_size)
			sim.Sim.Instance().get_logger().log_packet_state(self,'PKT_CRPTD',packet_size)



		 
		