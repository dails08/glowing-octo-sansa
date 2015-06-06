import zmq
import random
import sys
import time

port1 = sys.argv[1]
port2 = sys.argv[2]

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:%s" % port1)

answerer = context.socket(zmq.REP)
answerer.bind("tcp://*:%s" % port2)

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print "%d %d" % (topic, messagedata)
    publisher.send("%d %d" % (topic, messagedata))
    time.sleep(1)
