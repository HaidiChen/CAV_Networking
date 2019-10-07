import paho.mqtt.client as mqtt
import json

BROKER_URL_FILE = '../bip/ip.txt'
broker_url = ""
with open(BROKER_URL_FILE, 'r') as f:
    broker_url = f.readline().rstrip()

broker_port = 1883

OUTPUT_FOLDER = '../output/'

filename = 'hello'

def on_connect(client, userdata, flags, rc):
    pass
    print('connected with result code', rc)

def on_message_filename(client, userdata, message):
    global filename
    filename = message.payload.decode()
    print('filename reset to ', filename)

def on_message_result(client, userdata, message):
    global filename
    with open(OUTPUT_FOLDER + filename, 'wb') as f:
        f.write(message.payload)

    print('file received')

"""
def on_message(client, userdata, message):
    data = message.payload.decode()
    filename = data.split(',')[0]
    with open(OUTPUT_FOLDER + filename, 'wb') as f:
        f.write(base64.b64decode(data.split(',')[1]))
"""

client = mqtt.Client()
client.on_connect = on_connect
#client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe('filename', qos=2)
client.subscribe('result', qos=2)
#client.subscribe('file', 0)

client.message_callback_add('filename', on_message_filename)
client.message_callback_add('result', on_message_result)

client.loop_forever()
