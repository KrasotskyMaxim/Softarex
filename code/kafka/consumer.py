from kafka import KafkaConsumer
import json

def get_user(filename, labels):
    try:
        with open('log.json', 'a') as f:
        # f.write(f"{filename}\n\n")
            json.dump(labels, f, indent=4)
        print("Log write in file!")
    except Exception as e:
        print(e.__str__())
    

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='192.168.0.10:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))