import sys
import os
import zmq
import random

port = "5556"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

server_addr = os.getenv('PUB_SERVER_PORT', None)
if not server_addr:
  print "Ouchie..."
  sys.exit(-1)

print "Found server @ %s" % server_addr
socket.connect (server_addr)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = random.randrange(9999,10005)
print "Collecting updates from weather server for Zipcode %d" % topicfilter
socket.setsockopt(zmq.SUBSCRIBE, str(topicfilter))

# Process 5 updates
total_value = 0
for update_nbr in range (5):
  string = socket.recv()
  topic, messagedata = string.split()
  total_value += int(messagedata)
  print topic, messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr)
