import publisher
import broker

def main():
    broker_inst = broker.Broker()
    publisher_inst = publisher.Publisher(broker_inst)

    topic = 'xx'

    publisher_inst.pub2(topic)

if __name__ == "__main__":
    main()

