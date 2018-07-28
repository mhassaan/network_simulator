import csv 
from itertools import islice
import matplotlib.pyplot as plt
import math
class Result:
  def __init__(self,duration):
    self.duration = duration

  
  def throughput_by_load(self):
    tp_by_load = []
    cont_throughput= []
    for load in [10,210,510,1510]:
      for seed in range(0,10):
        tp = 0
        reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
        for row in reader:
          if ((row['event'].strip() == "PKT_RCVD")):
            size = row['size'].strip()
            size = float(size)
            tp = (tp +(size*8))
        tp = (tp/self.duration)/1024**2
        cont_throughput.append(tp)
      total_throughput_per_load = sum(cont_throughput)
      cont_throughput = []
      tp_by_load.append(total_throughput_per_load)
    return tp_by_load
  
  def throughput_by_node(self,node,load):
    cont_throughput = []
    for seed in range(0,10):
      reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
      tp = 0
      for row in reader:
        if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_RCVD")):
          size = row['size'].strip()
          size = float(size)
          tp = (tp +(size*8))
      tp = (tp/self.duration)/1024**2
      cont_throughput.append(tp)
    return cont_throughput


  def loss_rate_by_node(self,node,load):
    loss_rate_cont = []
    for seed in range(0,10):
      loss_pkt_count = 0
      sent_pkt_count = 0
      reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
      for row in reader:
        if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "LOSS_PKT")):
          loss_pkt_count +=1
        if ((row['src'].strip() == str(node)) and (row['event'].strip() == "SCHD_START_TX")):
          sent_pkt_count +=1        
      if loss_pkt_count > 0:
        loss_rate = loss_pkt_count/sent_pkt_count
      else:
        loss_rate = 0 

      loss_rate_cont.append(loss_rate)
    return loss_rate_cont
    
  def collision_rate_by_node(self,node,load):
    collision_cont = []
    for seed in range(0,10):
      crpt_count = 0
      rcvd_count = 0
      reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
      for row in reader:
        if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_RCVD")):
          rcvd_count+=1
        if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_CRPTD")):
          crpt_count+=1
      print("Received count is %d for node %d at load %d and seed %d" %(rcvd_count,node,load,seed))
      rate = rcvd_count+crpt_count
      if rate == 0:
        collide_rate = 0
      else: 
        collide_rate = (crpt_count/rate)

      collision_cont.append(collide_rate)

    return collision_cont

  def average_collision_rate(self,load):
    collision_cont = {}
    for node in range(1,11):
      crpt_count = 0
      rcvd_count = 0
      for seed in range(0,10):
        reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
        for row in reader:
          if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_RCVD")):
            rcvd_count+=1
          if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_CRPTD")):
            crpt_count+=1
        rate = rcvd_count+crpt_count
      if rate == 0:
        collide_rate = 0
      else: 
        collide_rate = (crpt_count/rate)
        collide_rate = collide_rate/10  

      collision_cont[node] = collide_rate

    return collision_cont

  def average_drop_rate(self,load):
    drop_rate_cont = {}
    for node in range(1,11):
      arrival_pkt_count=0
      drop_pkt_count = 0
      for seed in range(0,10):
        reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
        for row in reader:
          if ((row['src'].strip() == str(node)) and (row['event'].strip() == "ARRIVAL")):
            arrival_pkt_count+=1
          if ((row['src'].strip() == str(node)) and (row['event'].strip() == "DROP_PKT")):
            drop_pkt_count+=1

      if arrival_pkt_count > 0:
        drop_rate = drop_pkt_count/arrival_pkt_count
        drop_rate = drop_rate/10
      else:
        drop_rate = 0 
      drop_rate_cont[node] = drop_rate
    return drop_rate_cont
  
  def average_throughput_by_node(self,load):
    cont_throughput = {}
    temp_tp = []
    for node in range(1,11):
      temp_tp = []
      for seed in range(0,10):
        reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
        tmp_tp = 0
        for row in reader:
          if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "PKT_RCVD")):
            size = row['size'].strip()
            size = float(size)
            tmp_tp = (tmp_tp +(size*8))
        tmp_tp = (tmp_tp/self.duration)/1024**2
        temp_tp.append(tmp_tp)
      cont_throughput[node] = sum(temp_tp)/10
    return cont_throughput

  def average_loss_rate(self,load):
    loss_rate_cont = {}
    for node in range(1,11):
      loss_pkt_count = 0
      sent_pkt_count = 0
      for seed in range(0,10):
        reader = csv.DictReader(open("logger"+str(seed)+"-"+str(load)+".csv"))
        for row in reader:
          if ((row['dst'].strip() == str(node)) and (row['event'].strip() == "LOSS_PKT")):
            loss_pkt_count +=1
          if ((row['src'].strip() == str(node)) and (row['event'].strip() == "SCHD_START_TX")):
            sent_pkt_count +=1        
      if loss_pkt_count > 0:
        loss_rate = loss_pkt_count/sent_pkt_count
        loss_rate = loss_rate/10
      else:
        loss_rate = 0 

      loss_rate_cont[node] = loss_rate
    return loss_rate_cont

