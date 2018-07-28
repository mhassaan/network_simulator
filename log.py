import sim
from events import Events

class Log:
  def __init__(self,output_file):
    self.output_file = open(output_file,'w')
    self.output_file.write("time,src,dst,event,size\n")
    self.simulator = sim.Sim.Instance()
  
  def log_packet_arrival(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'ARRIVAL',pkt_size))


  def log_start_transmission(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'START_TX',pkt_size))
    
  def log_end_transmission(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'END_TX',pkt_size))

  def log_start_reception(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'START_RX',pkt_size))
  
  def schedule_start_reception(self,source,reception_time,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(reception_time,source.get_node_id(),source.get_node_id(),'SCHD_START_RX',pkt_size))

  def schedule_end_reception(self,source,reception_time,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(reception_time,source.get_node_id(),source.get_node_id(),'SCHD_ED_RX',pkt_size))

  def schedule_start_transmission(self,source,start_transmission_time,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(start_transmission_time,source.get_node_id(),source.get_node_id(),'SCHD_START_TX',pkt_size))

  def schedule_end_transmission(self,source,dst,end_transmission_time,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(end_transmission_time,source.get_node_id(),dst.get_node_id(),'SCHD_END_TX',pkt_size))

  def log_end_reception(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'END_RX',pkt_size))
  
  def log_packet_drop(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'DROP_PKT',pkt_size))

  def log_packet_loss(self,source,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),'LOSS_PKT',pkt_size))

  def log_packet_state(self,source,state,pkt_size):
    self.output_file.write("%f, %d, %d, %s, %d\n"%(self.simulator.get_time(),source.get_node_id(),source.get_node_id(),state,pkt_size))