import zmq
import random
import sys
import time

port1 = sys.argv[1]


context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:%s" % port1)

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print "%d %d" % (topic, messagedata)
    publisher.send("%d %d" % (topic, messagedata))
    time.sleep(1)
