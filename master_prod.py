import zmq
import time
import sys

def master():
	word = sys.argv[1]
	numWord = sys.argv[2]
	context = zmq.Context()
		
	publisher = context.socket(zmq.PUB)
	publisher.bind("tcp://*:5555")
	
	receiver = context.socket(zmq.PULL)
	receiver.bind("tcp://*:5556")
	
	for i in range(int(numWord)):
		print str(i)+": "+word
		publisher.send("READY_FOR_NEXT_WORD")
		publisher.send(word)
		word = receiver.recv()
	publisher.send("EXIT_NOW")
		
		
master()
