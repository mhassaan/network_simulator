class Packet:
  __packet_id = 1
  PKT_UNDER_TRANSMISSION = 0 
  PKT_TRANSMITTED = 1
  PKT_CORRUPTED = 2

  def __init__(self,pkt_size,duration):
    self.id = Packet.__packet_id
    self.size = pkt_size
    self.duration = duration
    self.state = Packet.PKT_UNDER_TRANSMISSION
  
  def set_state(self, state):
    self.state = state
  
  def get_state(self):
    return self.state
  
  def get_duration(self):
    return self.duration
  
  def get_packet_id(self):
    return self.id

  def get_packet_size(self):
    return self.size
     
  def log_packet_state(self):
    if self.get_state == Packet.PKT_UNDER_TRANSMISSION:
      t = "Packet %r under transmission."
    elif self.state == Packet.PKT_TRANSMITTED:
      t = "Packet %r transmitted successfully."
    elif self.state == Packet.PKT_CORRUPTED:
      t = "Packet %r got corrupteed."
    print(t %(self.get_packet_id()))
