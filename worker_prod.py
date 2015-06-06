import zmq
import random
import zipfile
import sys

def worker(workerID, fileFirst, fileLast):
	print "Worker "+ str(workerID) + " started"
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect("tcp://10.122.102.45:5555")
	receiver.setsockopt(zmq.SUBSCRIBE,'')
	
	pusher = context.socket(zmq.PUSH)
	pusher.connect("tcp://10.122.102.45:5556")
	found = False
	done = False
	while True:
		word = receiver.recv()
		if word == "EXIT_NOW":
			print "Worker "+str(workerID)+" exiting"
			sys.exit()
		for i in range(int(fileFirst), int(fileLast)+1):
			if done:
				break
			if receiver.recv(0) == "READY_FOR_NEXT_WORD":
				break;
			filename = "/gpfs/gpfsfpo/"+str(i)+".zip"
			currentFile = zipfile.open(filename)
			for li in currentFile.namelist():
				if done:
					break
				options = {}
				for line in li.read():
					splits = string.split(line, "\t")
					thisWord = string.split(splits[0])
					nextWord = string.split(splits[1])
					if (thisWord == word):
						found = True
						if not thisWord in options:
							options[thisWord] = splits[2]
						else:
							options[thisWord] = options[thisWord] + splits[2]
					else if found:
						#picks the first one for now
						pusher.send(options.keys()[0])
						done = True
						break
			currentFile.close()			
					

worker()
