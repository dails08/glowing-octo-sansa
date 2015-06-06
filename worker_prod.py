import zmq
import random
import zipfile

def worker(workerID, fileFirst, fileLast):
	print "Worker "+ str(workerID) + " started"
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect("tcp://10.122.102.45:5555")
	receiver.setsockopt(zmq.SUBSCRIBE,'')
	
	pusher = context.socket(zmq.PUSH)
	pusher.connect("tcp://10.122.102.45:5556")
	
	while True:
		word = receiver.recv()
		if word == "EXIT_NOW":
			break
		for 
	
	
	while True:
		print "Listening..."
		msg = receiver.recv()
		print "Worker #"+str(worker_id)+" received message:\n"+msg

worker()
