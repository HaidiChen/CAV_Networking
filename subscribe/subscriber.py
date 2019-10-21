import paho.mqtt.client as mqtt
import os

# constant variable
OUTPUT_FOLDER = '../output/'

# class for subscriber
class Subscriber(object):

    def __init__(self, broker):
        self._filename = 'hello'
        self._client = mqtt.Client()
        self._qos = 0
        self._client.on_connect = self._on_connect
        self._client.connect(broker.get_url(), broker.get_port())

    def _on_connect(self, client, userdata, flags, rc):
        print('connected with result code', rc)

    def _on_message_filename(self, client, userdata, message):
        self._filename = message.payload.decode()
        print('filename reset to ', self._filename)

    def _on_message_result(self, client, userdata, message):
        with open(os.path.join(OUTPUT_FOLDER, self._filename), 'wb') as f:
            f.write(message.payload)

        print('file received')

    def sub(self, topics):
        for i in range(0, len(topics), 2):
            self._client.subscribe(topics[i], self._qos)
            self._client.subscribe(topics[i + 1], self._qos)

            self._client.message_callback_add(topics[i],
                    self._on_message_filename)
            self._client.message_callback_add(topics[i + 1],
                    self._on_message_result)

        self._client.loop_forever()

