import os
import random
from paho.mqtt import client as mqtt_client

class mqtt:
    def __init__(self):
        pass
    
    @classmethod
    def connect_mqtt(self) -> mqtt_client:
        client_id = f'subscribe-{random.randint(0,1000)}'
        broker = os.environ.get('mqtt-broker')
        port = int(os.environ.get('mqtt-port',1883))
        username = os.environ.get('mqtt-username')
        password = os.environ.get('mqtt-password')
        def on_connect(client, userdata, flags, rc):
            if rc != 0:
                print("Failed to connect, return code %d\n",rc)
        client = mqtt_client.Client(client_id)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client
    
    @classmethod
    def subscribe(self, client: mqtt_client, on_message):
        topic = 'home/#'
        client.subscribe(topic)
        client.on_message = on_message