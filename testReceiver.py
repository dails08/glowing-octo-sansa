import sys
import zmq

port1 = sys.argv[1]

# Socket to talk to server
context = zmq.Context()
subscriber = context.socket(zmq.SUB)

subscriber.connect ("tcp://10.122.102.45:%s" % port1)
subscriber.setsockopt(zmq.SUBSCRIBE, '')


# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print topic, messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr)
