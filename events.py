class Events:
	'''
	Types of events that can occur during simulation.
	'''
	# Start transmitting the packet.
	START_TRANSMISSION = 0
	# End transmitting the packet.
	END_TRANSMISSION = 1
	# Start Receiving Packet
	START_RECEPTION = 2
	# End Receving Packet
	END_RECEPTION = 3
	# Packet Arrival
	PKT_ARRIVAL = 4
