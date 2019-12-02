import paho.mqtt.client as mqtt
import json
import base64
import os

class Subscriber(object):

    # the folder where received files go to
    OUTPUT_FOLDER = '../output/'

    def __init__(self):
        self._client = mqtt.Client()
        self._qos = 0
        self._message = {}
        self._client.on_connect = self._on_connect

    def _on_connect(self, client, userdata, flags, rc):
        print('connected with result code', rc)

    def connect_broker(self, broker):
        self._client.connect(broker.get_url(), broker.get_port(), 1800)

    def subscribe_to_topics(self, topics):
        for topic in topics:
            self._subscribe_to_one_topic(topic)

        self._client.loop_forever()

    def _subscribe_to_one_topic(self, topic):
        self._client.subscribe(topic, self._qos)
        self._client.message_callback_add(topic, self._on_receive_data)

    def _on_receive_data(self, client, userdata, message):
        self._extract_message(message)
        self._recover_received_file()
        self._print_name_of_received_file()

    def _extract_message(self, message):
        decoded = str(message.payload.decode("utf-8", "ignore"))
        self._message = json.loads(decoded)
   
    def _recover_received_file(self):
        filename = self._message['filename']
        self._write_to_file(filename)

    def _write_to_file(self, filename):
        with open(os.path.join(Subscriber.OUTPUT_FOLDER, filename), 'wb') as f:
            f.write(base64.b64decode(self._message['imageString']))

    def _print_name_of_received_file(self):
        print(self._message['filename'])


