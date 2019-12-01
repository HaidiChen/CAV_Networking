import paho.mqtt.client as mqtt
import json
import base64
import os

# class for subscriber
class Subscriber(object):

    # constant variable
    OUTPUT_FOLDER = '../output/'

    def __init__(self):
        self._client = mqtt.Client()
        self._qos = 0
        self._message = {}
        self._client.on_connect = self._on_connect

    def connect_broker(self, broker):
        self._client.connect(broker.get_url(), broker.get_port(), 1800)

    def _on_connect(self, client, userdata, flags, rc):
        print('connected with result code', rc)

    def _on_receive_data(self, client, userdata, message):
        self._extract_message(message)
        self._recover_image()
        self._print_name_of_received_file()
    
    def _recover_image(self):
        filename = self._message['filename']
        with open(os.path.join(Subscriber.OUTPUT_FOLDER, filename), 'wb') as f:
            f.write(base64.b64decode(self._message['imageString']))

    def _print_name_of_received_file(self):
        print(self._message['filename'])

    def _extract_message(self, message):
        decoded = str(message.payload.decode("utf-8", "ignore"))
        self._message = json.loads(decoded)

    def subscribe_to_topics(self, topics):
        for topic in topics:
            self._subscribe_to_one_topic(topic)

        self._client.loop_forever()

    def _subscribe_to_one_topic(self, topic):
        self._client.subscribe(topic, self._qos)
        self._client.message_callback_add(topic, self._on_receive_data)

