import json
import time
import datetime
import config
from kafka import KafkaProducer


class Producer:
    def __init__(self, to_save: str = 'log.json', bootstrap_servers: str = "127.0.0.1:9095") -> None:
        # value_serializer=lambda m: json.dumps(m).encode()
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda m: json.dumps(m).encode()
            )
        self.to_save = to_save
        f = open(self.to_save, 'w')
        f.close()

    def send(self, user) -> list:
        ''' Return an emotions of registed users '''
        self.kafka_producer.send(config.LABEL_TOPIC, user)
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
