import json
import configs.config as config
from kafka import KafkaProducer


class Producer:
    def __init__(self, bootstrap_servers: str = "127.0.0.1:9095") -> None:
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=config.SERVER,
            # value_serializer=lambda m: json.dumps(m).encode()
            )

    def send(self, topic, user) -> list:
        ''' Return an emotions of registed users '''
        self.kafka_producer.send(topic, user)
      
    
