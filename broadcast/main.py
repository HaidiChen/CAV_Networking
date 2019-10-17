import publisher
import broker

def main():
    broker_inst = broker.Broker()
    publisher_inst = publisher.Publisher(broker_inst)
    publisher_inst.pub('feedback_filename', 'feedback_result')

if __name__ == "__main__":
    main()

