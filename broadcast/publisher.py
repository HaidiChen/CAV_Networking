import paho.mqtt.client as mqtt
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
            fname = fileList[i]

            start_time = time.time()

            with open(os.path.join(SOURCE_FOLDER, fname), 'rb') as f:
                filepayload = f.read()
                filebyte = bytearray(filepayload)
                for j in range(0, len(topics), 2):
                    self._client.publish(topics[j], fname, self._qos)
                    self._client.publish(topics[j + 1], filebyte, self._qos)

            print('Broadcasting Time: {}'.format(time.time() - start_time))

            i += 1

        self._client.loop_stop()

