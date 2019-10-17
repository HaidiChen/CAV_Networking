import subscriber
import broker

def main():
    broker_inst = broker.Broker()
    subscriber_inst = subscriber.Subscriber(broker_inst)
    subscriber_inst.sub('feedback_filename', 'feedback_result')

if __name__ == "__main__":
    main()

