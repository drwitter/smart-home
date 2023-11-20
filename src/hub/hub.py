from src.readers.mqtt import mqtt
from src.writers.postgres import postgres

class hub:
    def _init__(self):
        pass

    def start(self):
        client = mqtt.connect_mqtt()
        mqtt.subscribe(client, self.on_message)
        client.loop_forever()

    def on_message(self, client, userdata, msg):
        writer = postgres()
        writer.connect()
        writer.write(self.decode_message(msg))
        writer.close()

    def decode_message(self, msg) -> dict:
        topic = msg.topic
        split_topic = topic.split('/')
        sensor = split_topic[1]
        room = split_topic[2]
        value = msg.payload.decode()
        return {'sensor': sensor, 'room': room, 'value': value}
