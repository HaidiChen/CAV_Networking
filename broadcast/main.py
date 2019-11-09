import publisher
import broker

def main():
    broker_inst = broker.Broker()
    publisher_inst = publisher.Publisher(broker_inst)

    # for MQTT_Expose
    topics = ['feedback_filename', 'feedback_result']

    # for N2N
#    topics = ['filename_3', 'result_3']

#    publisher_inst.pub(topics)
    publisher_inst.pub2('img')

if __name__ == "__main__":
    main()

