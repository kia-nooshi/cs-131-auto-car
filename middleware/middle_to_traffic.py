import zmq
import time

# setup for subscriber
context_subscriber = zmq.Context()
socket_subscriber = context_subscriber.socket(zmq.SUB)
socket_subscriber.connect('tcp://192.168.254.78:2000')
# socket channel for publisher of traffic light
socket_subscriber.setsockopt_string(zmq.SUBSCRIBE, '10011')

# setup publisher middleware to jetbot
context_publisher = zmq.Context()
socket_publisher = context_publisher.socket(zmq.PUB)
socket_publisher.bind('tcp://*:2001')
topic_publisher = 11000

# logic for reading msgs

while(True):
    time.sleep(1)
    # if there is no message this get hung up
    message = socket_subscriber.recv()
    if len(message) > 0:
        socket_publisher.send_string('%d %s' % (topic_publisher, message))
        print(f'Traffic light Status: {message}')