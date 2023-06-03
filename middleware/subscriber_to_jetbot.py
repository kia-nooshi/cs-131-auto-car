import zmq
import time


# setup for subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://192.168.254.133:2000')
# socket channel for publisher of traffic light
socket.setsockopt_string(zmq.SUBSCRIBE, '10001')

# logic for reading msgs

while(True):
    try: 
        # if there is no message this get hung up
        message = socket.recv()
        print(message)
    except:
        print('no msg')
        context.destroy()
        time.sleep(1)