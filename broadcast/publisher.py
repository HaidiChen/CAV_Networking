import paho.mqtt.client as mqtt
import json
import base64
import os
import time

# class for publishing
class Publisher(object):

    # Constant variables
    SOURCE_FOLDER = '../result/'

    def __init__(self):
        self._client = mqtt.Client()
        self._qos = 0
        self._message = {}
        self._filesInSourceFolder = []

    def connect_broker(self, broker):
        self._client.connect(broker.get_url(), broker.get_port())

    def publish_on_topics(self, topics):
        self._start_publishing_procedure()
        self._publish_message_on_topics(topics)
        self._stop_publishing_procedure()

    def _start_publishing_procedure(self):
        self._client.loop_start()

    def _stop_publishing_procedure(self):
        self._client.loop_stop()

    def _publish_message_on_topics(self, topics):
        self._update_files_in_source_folder()

        for namedFile in self._filesInSourceFolder:
            self._prepare_message(namedFile)
            self._attach_to_topics(topics)

    def _update_files_in_source_folder(self):
        self._filesInSourceFolder = os.listdir(Publisher.SOURCE_FOLDER)

    def _prepare_message(self, filename):
        self._message['filename'] = filename

        with open(os.path.join(Publisher.SOURCE_FOLDER, filename), 'rb') as f:
            filepayload = f.read()
            self._message['imageString'] = base64.b64encode(filepayload).decode()

    def _attach_to_one_topic(self, topic):
        self._client.publish(topic, json.dumps(self._message), self._qos)

    def _attach_to_topics(self, topics):
        for topic in topics:
            self._attach_to_one_topic(topic)

