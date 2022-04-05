from kafka import KafkaConsumer
import json

def get_user(filename, labels):
    try:
        f = open('log.txt', 'a')
        f.write(f"{filename}\n\n")
        for label in labels:
            msg = f'{label[0][1][:5]}, ... -  {label[1]}\n\n'
            f.write(msg)
        print("Log write in file!")
    except Exception as e:
        print(e.__str__())
    finally:
        f.close()

    

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='192.168.0.10:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))