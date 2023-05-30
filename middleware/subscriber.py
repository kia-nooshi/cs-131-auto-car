import zmq
import time

# setup for subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://192.168.254.174:2000')
socket.setsockopt_string(zmq.SUBSCRIBE, '10001')

# logic for reading msgs

while(True):
    try: 
        # if there is no message this get hung up
        message = socket.recv(flags=NOBLOCK)
        print(message)
    except:
        time.sleep(1)