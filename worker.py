import zmq
import random

def worker():
	worker_id = random.randrange(1,1000)
	print "Worker "+ str(worker_id) + " started"
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect("tcp://localhost:5557")
	while True:
		print "Listening..."
		msg = receiver.recv()
		print "Worker #"+str(worker_id)+" received message:\n"+msg

worker()
