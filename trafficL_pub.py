import serial 
import time

import zmq
from time import sleep

# setting up Publisher and socket. (tutorial test)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:2000')

topic = 10011
messages = [100,200,300]
curMsg = 0

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


while True:
    try:
        data = arduino.readline()
        if data:
            print(data)
            print('Hi Arduino')

        sleep(1)
        socket.send_string('%d %s' % (topic, data))
        if(curMsg == 2):
            curMsg = 0
        else:
            curMsg += 1

    except:
        arduino.close()





