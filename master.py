import zmq
import time

def master():
	context = zmq.Context()
	publisher = context.socket(zmq.PUB)
	publisher.bind("tcp://*:5557")
	
	puller = context.socket(zmq.PULL)
	puller.bind("tcp://*:5559")
	for i in range(1000):
		print "Sending message "+str(i)
		publisher.send("This is message "+ str(i))
		print "Waiting for response..."
		response = puller.recv()
		print "Response received"
		time.sleep(1)
		
master()
