import zmq
from time import sleep

# setting up Publisher and socket. (tutorial test)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')
topic = 10001
messages = [100,200,300]
curMsg = 0

while(True):
    sleep(1)
    socket.send_string('%d %d' % (topic, messages[curMsg]))
    if(curMsg == 2):
        curMsg = 0
    else:
        curMsg += 1

