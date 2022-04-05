from kafka import KafkaProducer
# import json
import consumer
import time


# def json_serializer(data):
#     return json.dumps(data).encode("utf-8")


# producer = KafkaProducer(bootstrap_servers=['192.168.0.10:9092'],
#                          value_serializer=json_serializer)

def send(filename, user) -> list:
    ''' Return an emotions of registed users '''
    consumer.get_user(filename, user)


if __name__ == "__main__":
    # while True:
    #     registered_user = get_emotion_labels()
    #     print(registered_user)
    #     # producer.send("registered_user", registered_user)
    #     time.sleep(2)
    pass 