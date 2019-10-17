import paho.mqtt.client as mqtt
import os
import time

# Constant variables
OUTPUT_FOLDER = '../result/'

# class for publishing
class Publisher(object):

    def __init__(self, broker):
        self._client = mqtt.Client()
        self._qos = 0
        self._client.connect(broker.get_url(), broker.get_port())

    def pub(self, topic1, topic2):
        self._client.loop_start()

        fileList = os.listdir(OUTPUT_FOLDER)
        i = 0

        while i < len(fileList):
            fname = fileList[i]

            start_time = time.time()

            with open(os.path.join(OUTPUT_FOLDER, fname), 'rb') as f:
                filepayload = f.read()
                filebyte = bytearray(filepayload)
                self._client.publish(topic1, fname, self._qos)
                self._client.publish(topic2, filebyte, self._qos)

            print('Broadcasting Time: {}'.format(time.time() - start_time))

            i += 1

        self._client.loop_stop()

