from subscriber import Subscriber
from broker import Broker

def main():
    broker = Broker()
    subscriber = Subscriber()

    subscriber.connect_broker(broker)

    topics = ["1", "2", "3", "4", '5', '6', '7', '8', '9']

    subscriber.subscribe_to_topics(topics)

if __name__ == "__main__":
    main()

