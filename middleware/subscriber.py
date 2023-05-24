import zmq

# setup for subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2000')
socket.setsockopt_string(zmq.SUBSCRIBE, '10001')

# logic for reading msgs

while(True):
    message = socket.recv()
    print(message)