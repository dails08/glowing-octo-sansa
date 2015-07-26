import zmq
import time

def master():
	context = zmq.Context()
	publisher = context.socket(zmq.XPUB)
	publisher.bind("tcp://*:5557")
	
	listener = context.socket(zmq.REP)
	listener.bind("tcp://*:5559")

	time.sleep(2)

	for i in range(1000):
		print "Sending message "+str(i)
		publisher.send("This is message "+ str(i))
		print "Message sent."
		print "Waiting for response..."
		publisher.recv()
		print "Response received"
		
		
		
master()
