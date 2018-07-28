from events import Events

class Event:
	def __init__(self,event_time,event_type,source,destination,obj=None):
		self.event_time = event_time
		self.event_type = event_type
		self.source = source
		self.destination = destination
		self.obj = obj

	def get_event_time(self):
		return self.event_time

	def get_event_type(self):
		return self.event_type

	def get_event_source(self):
		return self.source

	def get_event_destination(self):
		return self.destination


	def get_object(self):
		# return the object attached to the Event
		return self.obj


	def dump_event(self):
		print ("Event time is %f" % self.event_time)
		t = ""
		if self.event_type == Events.START_TRANSMISSION:
			t = "Start-Transmission"
		elif self.event_type == Events.END_TRANSMISSION:
			t = "End-Transmission"
		elif self.event_type == Events.START_RECEPTION:
			t = "Start-Reception"
		elif self.event_type == Events.END_RECEPTION:
			t = "End-Reception"
		elif self.event_type == Events.PKT_ARRIVAL:
			t = "Packet-Arrival"
      
		print ("Event type: %s" %t)
		print ("Source Node: %r" %get_event_source())
		print ("Destination Node: %r" %get_event_destination())
