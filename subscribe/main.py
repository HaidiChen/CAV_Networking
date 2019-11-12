import subscriber
import broker

def main():
    broker_inst = broker.Broker()
    subscriber_inst = subscriber.Subscriber(broker_inst)

#    topics = ['feedback_filename', 'feedback_result']

    topics = ["1", "2", "3", "4", '5', '6', '7', '8', '9']

    subscriber_inst.sub(topics)

#    subscriber_inst.sub2('img')


if __name__ == "__main__":
    main()

