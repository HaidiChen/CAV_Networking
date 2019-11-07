import subscriber
import broker

def main():
    broker_inst = broker.Broker()
    subscriber_inst = subscriber.Subscriber(broker_inst)

    topics = ['feedback_filename', 'feedback_result']
    # for N2N 
#    topics = ["filename_1", "result_1", "filename_2", "result_2"]

    subscriber_inst.sub(topics)


if __name__ == "__main__":
    main()

