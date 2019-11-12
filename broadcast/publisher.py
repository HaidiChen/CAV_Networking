import paho.mqtt.client as mqtt
import json
import base64
import os
import time

# Constant variables
SOURCE_FOLDER = '../result/'

# class for publishing
class Publisher(object):

    def __init__(self, broker):
        self._client = mqtt.Client()
        self._qos = 0
        self._client.connect(broker.get_url(), broker.get_port())

    def pub(self, topics):
        self._client.loop_start()

        fileList = os.listdir(SOURCE_FOLDER)
        i = 0

        while i < len(fileList):
            data = {}
            fname = fileList[i]

            data['filename'] = fname

            with open(os.path.join(SOURCE_FOLDER, fname), 'rb') as f:
                filepayload = f.read()
                data['img'] = base64.b64encode(filepayload).decode()
                for j in range(0, len(topics)):
                    self._client.publish(topics[j], json.dumps(data), self._qos)

            i += 1

        self._client.loop_stop()

    def pub2(self, topics):
        self._client.loop_start()

        fileList = os.listdir(SOURCE_FOLDER)
        i = 0

        while i < len(fileList):
            data = {}
            fname = fileList[i]

            data['filename'] = fname

            with open(os.path.join(SOURCE_FOLDER, fname), 'rb') as f:
                filepayload = f.read()
                data['img'] = base64.b64encode(filepayload).decode()
                self._client.publish(topics, json.dumps(data), self._qos)

            i += 1

        self._client.loop_stop()

