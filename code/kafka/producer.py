import json, time, datetime
import config
import cv2
from kafka import KafkaProducer


class Producer:
    def __init__(self, bootstrap_servers: str = "127.0.0.1:9095") -> None:
        # value_serializer=lambda m: json.dumps(m).encode()
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=config.SERVER,
            # value_serializer=lambda m: json.dumps(m).encode()
            )

    def send(self, topic, user) -> list:
        ''' Return an emotions of registed users '''
        image = cv2.imread(user)
        retval, buffer = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY),40])
        if not retval:
            print("Error was occurred during image encoding") 
        value = buffer.tobytes()
        self.kafka_producer.send(topic, value)
        # try:
        #     with open(self.to_save, 'a') as f:
        #         json.dump(user, f, indent=4)
        #     print("Log write in file!")
        # except Exception as e:
        #     print(e.__str__())
    

if __name__ == "__main__":
    producer = Producer(bootstrap_servers= "127.0.0.1:9095")
    for i in range(100):
        data = {'num': i, 'ts': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        producer.send(user=data)
        time.sleep(2)
