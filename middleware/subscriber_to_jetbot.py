import zmq
import time
from google.cloud import pubsub_v1
from threading import Thread
from concurrent.futures import TimeoutError

def jetBot_to_middle():
    # setting up info for google cloud api
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path('cs-131-final-project', 'edge-to-cloud')
    
    
    # setup for subscriber
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://192.168.254.85:2000')
    # socket channel for publisher of traffic light
    socket.setsockopt_string(zmq.SUBSCRIBE, '10001')
    
    # logic for reading msgs
    while(True):
        try: 
            # if there is no message this get hung up
            message = socket.recv()
            if len(message) > 0:
                print(f'Msg from Jetbot 1 to fog: {message}')
                # Data must be a bytestring
                print('sending blocked command to cloud')
                data = f"Car 1 Stopped {message}".encode("utf-8")
                # When you publish a message, the client returns a future.
                future = publisher.publish(topic_path, data)
                future.result()
            #print(message)
        except:
            print('no msg')
            context.destroy()
            time.sleep(1)

#function that handles communication from fog to jetbot
def middle_to_jetbot(msg,socket):
    # <class 'google.cloud.pubsub_v1.subscriber.message.Message'>
    #print(type(msg))
    topic = 11011
    msgData = bytes.decode(msg.data)
    socket.send_string('%d %s' % (topic, msgData))
    print(f'Sent to Jetbot 1: {topic} {msgData}\n')
    #print(type(msgData))

def cloud_to_jetbot(socket):
    # gcloud setup
    # Number of seconds the subscriber should listen for messages
    timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path('cs-131-final-project', 'edge-sub')

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received from cloud {message}.\n")
        message.ack()
        # once msg recived relay to jetbot
        middle_to_jetbot(message,socket)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.

def cloud_sub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:2002')
    while True:
        cloud_to_jetbot(socket)
        time.sleep(1)

t1 = Thread(target = jetBot_to_middle)
t1.start()
t2 = Thread(target = cloud_sub())
t2.start()
