import zmq
import time
import sys

def master():
	word = sys.argv[1]
	numWord = sys.argv[2]
	port1 = int(sys.argv[3])
	port2 = int(sys.argv[4])
	context = zmq.Context()	
	publisher = context.socket(zmq.PUB)
	publisher.bind("tcp://*:%s" % port1)
	
	receiver = context.socket(zmq.REP)
	receiver.bind("tcp://*:%s" % port2)
	
	for i in range(int(numWord)):
		print str(i)+": "+word
		publisher.send("READY_FOR_NEXT_WORD")
		publisher.send(word)
		word = receiver.recv()
		receiver.send("Master IRO")
		time.sleep(1)
		print "Received: "+word
	publisher.send("EXIT_NOW")
		
		
master()
