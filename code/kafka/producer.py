from kafka import KafkaProducer
# import json
from data import get_emotion_labels
import time


# def json_serializer(data):
#     return json.dumps(data).encode("utf-8")


# producer = KafkaProducer(bootstrap_servers=['192.168.0.10:9092'],
#                          value_serializer=json_serializer)

def start_registed_users(path: str) -> list:
    ''' Return an emotions of registed users '''
    registed_users = get_emotion_labels(img_path=path)
    return registed_users


if __name__ == "__main__":
    # while True:
    #     registered_user = get_emotion_labels()
    #     print(registered_user)
    #     # producer.send("registered_user", registered_user)
    #     time.sleep(2)
    registered_user = get_emotion_labels()
    print(registered_user)