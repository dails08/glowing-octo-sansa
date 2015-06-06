import zmq
import time

def master():
	context = zmq.Context()
	zmq_socket = context.socket(zmq.PUB)
	zmq_socket.bind("tcp://*:5557")
	for i in range(1000):
		print "Sending message "+str(i)
		zmq_socket.send("This is message "+ str(i))
		time.sleep(1)
		
master()
