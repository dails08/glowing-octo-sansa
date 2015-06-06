import zmq
import random
import zipfile
import sys

def worker(workerID, fileFirst, fileLast):
	print "Worker "+ str(workerID) + " started"
	port1 = int(sys.argv[4])
	port2 = int(sys.argv[5])
	
	# Socket to talk to server
	context = zmq.Context()
	receiver = context.socket(zmq.SUB)
	receiver.connect ("tcp://10.122.102.45:%s" % port1)
	receiver.setsockopt(zmq.SUBSCRIBE, '')
	
	
	
	
	#pusher = context.socket(zmq.PUSH)
	#pusher.connect("tcp://10.122.102.45:%s" % port2)
	found = False
	done = False
	while True:
		print "Ready to receive"
		word = receiver.recv()
		print "Received order: "+word
		#if word == "EXIT_NOW":
			#print "Worker "+str(workerID)+" exiting"
			#sys.exit()
		#for i in range(int(fileFirst), int(fileLast)+1):
			#if done:
				#break
			#if receiver.recv(0) == "READY_FOR_NEXT_WORD":
				#break;
			#filename = "/gpfs/gpfsfpo/"+str(i)+".zip"
			#currentFile = zipfile.open(filename)
			#for li in currentFile.namelist():
				#if done:
					#break
				#options = {}
				#for line in li.read():
					#splits = string.split(line, "\t")
					#thisWord = string.split(splits[0])
					#nextWord = string.split(splits[1])
					#if (thisWord == word):
						#found = True
						#if not thisWord in options:
							#options[thisWord] = splits[2]
						#else:
							#options[thisWord] = options[thisWord] + splits[2]
					#elif found:
						##picks the first one for now
						#pusher.send(options.keys()[0])
						#done = True
						#break
			#currentFile.close()			
					

worker(sys.argv[1], sys.argv[2], sys.argv[3])
