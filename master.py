import zmq
import time

def master():
	context = zmq.Context()
	publisher = context.socket(zmq.PUB)
	publisher.bind("tcp://*:5557")
	for i in range(1000):
		print "Sending message "+str(i)
		publisher.send("This is message "+ str(i))
		time.sleep(1)
		
master()
