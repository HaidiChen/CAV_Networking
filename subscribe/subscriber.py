import paho.mqtt.client as mqtt
import json
import base64
import os

# class for subscriber
class Subscriber(object):

    # constant variable
    OUTPUT_FOLDER = '../output/'

    def __init__(self, broker):
        self._filename = 'hello'
        self._client = mqtt.Client()
        self._qos = 0
        self._client.on_connect = self._on_connect
        self._client.connect(broker.get_url(), broker.get_port(), 1800)

    def _on_connect(self, client, userdata, flags, rc):
        print('connected with result code', rc)

    def _on_message_filename(self, client, userdata, message):
        self._filename = message.payload.decode()
        print('filename reset to ', self._filename)

    def _on_message_result(self, client, userdata, message):
        with open(os.path.join(Subscriber.OUTPUT_FOLDER, self._filename), 'wb') as f:
            f.write(message.payload)

        print('file received')

    def _on_json_data(self, client, userdata, message):
        decoded = str(message.payload.decode("utf-8", "ignore"))
        data = json.loads(decoded)
        fname = data['filename']
        print(fname)
        with open(os.path.join(Subscriber.OUTPUT_FOLDER, fname), 'wb') as f:
            f.write(base64.b64decode(data['img']))

    def sub(self, topics):
        for i in range(0, len(topics)):
            self._subscribe_helper(topics[i])
#            self._client.subscribe(topics[i], self._qos)
#
#            self._client.message_callback_add(topics[i], self._on_json_data)

        self._client.loop_forever()

    def sub2(self, topics):
        self._subscribe_helper(topics)
#        self._client.subscribe(topics, self._qos)
#
#        self._client.message_callback_add(topics, self._on_json_data)

        self._client.loop_forever()

    def _subscribe_helper(self, topic):
        self._client.subscribe(topic, self._qos)
        self._client.message_callback_add(topic, self._on_json_data)

