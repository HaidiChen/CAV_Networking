# constant variable
BROKER_URL_FILE = '../bip/ip.txt'

# class for broker
class Broker(object):
    
    def __init__(self):
        self._url = ''
        self._port = 1883
        with open(BROKER_URL_FILE, 'r') as f:
            urlport = f.readline().rstrip()
            urlport = urlport.split(':')
            self._url = urlport[0]
            self._port = int(urlport[1])

    def get_url(self):
        return self._url

    def get_port(self):
        return self._port

def main():
    broker_inst = Broker()
    print(broker_inst.get_url())
    print(broker_inst.get_port())

if __name__ == "__main__":
    main()
