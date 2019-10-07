# broadcasting the result
import paho.mqtt.client as mqtt
import os
import time

OUTPUT_FOLDER = '../result/'
BROKER_URL_FILE = '../bip/ip.txt'

broker_url = ''
with open(BROKER_URL_FILE, 'r') as f:
    broker_url = f.readline().rstrip()

broker_port = 1883

client = mqtt.Client('PUB')
client.connect(broker_url, broker_port)
client.loop_start()

# part 2). broadcast the data
fileList = os.listdir(OUTPUT_FOLDER)
i = 0

while i < len(fileList):
    fname = fileList[i]
    
    start_time = time.time()
    with open(OUTPUT_FOLDER + fname, 'rb') as f:
        filepayload = f.read()
        filebyte = bytearray(filepayload)
        client.publish('filename', fname, 2)
        client.publish('result', filebyte, 2)

    print('Time___________broadcasting time: {}'.format(time.time() - start_time))
    i += 1

client.loop_stop()
#for fname in fileList:
#    os.remove(OUTPUT_FOLDER + fname)
#os.remove(OUTPUT_FOLDER + fname)
#fileList = os.listdir(OUTPUT_FOLDER)
