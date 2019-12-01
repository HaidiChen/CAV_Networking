from publisher import Publisher
from broker import Broker

def main():
    broker = Broker()
    publisher = Publisher()

    publisher.connect_broker(broker)

    topics = ['1']

    publisher.publish_on_topics(topics)

if __name__ == "__main__":
    main()

