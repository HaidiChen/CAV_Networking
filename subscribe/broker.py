class Broker(object):
    
    BROKER_URL_FILE = '../bip/ip.txt'

    def __init__(self):
        self._set_broker_url_port()

    def _set_broker_url_port(self):
        urlport = self._get_url_port_from_file()
        self._url = urlport[0]
        self._port = int(urlport[1])

    def _get_url_port_from_file(self):
        with open(Broker.BROKER_URL_FILE, 'r') as f:
            urlport = f.readline().rstrip()
            urlport = urlport.split(':')

        return urlport

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
