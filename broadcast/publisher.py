import paho.mqtt.client as mqtt
import json
import base64
import os
import time

class Publisher(object):

    # the folder where to-be-broadcasted files store 
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
        self._publish_files(topics)

    def _update_files_in_source_folder(self):
        self._filesInSourceFolder = os.listdir(Publisher.SOURCE_FOLDER)

    def _publish_files(self, topics):
        for named_file in self._filesInSourceFolder:
            self._prepare_message(named_file)
            self._attach_to_topics(topics)

    def _prepare_message(self, filename):
        self._set_value_of_key_filename(filename)
        self._set_value_of_key_imageString(filename)

    def _set_value_of_key_filename(self, filename):
        self._message['filename'] = filename

    def _set_value_of_key_imageString(self, filename):
        with open(os.path.join(Publisher.SOURCE_FOLDER, filename), 'rb') as f:
            filepayload = f.read()
            self._message['imageString'] = base64.b64encode(filepayload).decode()

    def _attach_to_topics(self, topics):
        for topic in topics:
            self._attach_to_one_topic(topic)

    def _attach_to_one_topic(self, topic):
        self._client.publish(topic, json.dumps(self._message), self._qos)

