import zmq
import random

def worker():
	worker_id = random.randrange(1,1000)
	print "Worker "+ str(worker_id) + " started"
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect("tcp://10.122.102.45:5557")
	receiver.setsockopt(zmq.SUBSCRIBE,'')
	
	pusher = context.socket(zmq.PUSH)
	pusher.connect("tcp://10.122.102.45:5559")
	
	while True:
		print "Listening..."
		msg = receiver.recv()
		print "Worker #"+str(worker_id)+" received message:\n"+msg

worker()
