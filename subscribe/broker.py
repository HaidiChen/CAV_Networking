# constant variable
BROKER_URL_FILE = '../bip/ip.txt'

# class for broker
class Broker(object):
    
    def __init__(self):
        self._url = ''
        with open(BROKER_URL_FILE, 'r') as f:
            self._url = f.readline().rstrip()
        self._port = 1883

    def get_url(self):
        return self._url

    def get_port(self):
        return self._port

    def set_urlport(self, url, port):
        self._url = url
        self._port = port

