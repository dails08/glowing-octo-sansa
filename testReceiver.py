import sys
import zmq

port = "5555"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://10.122.102.45:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, '')

# Subscribe to zipcode, default is NYC, 10001
#topicfilter = "10001"
#socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print topic, messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr)
