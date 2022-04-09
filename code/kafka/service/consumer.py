import cv2
import numpy as np
from kafka import KafkaConsumer


class Consumer:
    def __init__(self, *topics, **configs) -> None:
        # print(topics)
        # print(configs)
        self.kafka_consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=configs["bootstrap_servers"],
            auto_offset_reset='earliest'
            )
        self.index = 0
        self.filenames = []

    # def subscribe(self, topic):
    #     self.kafka_consumer.subscribe(topic)
        
    def poll(self, msg: str):
        ''' Send a converted image to classificator '''
        image_name = list(msg.keys())[0]
        msg_value = msg[image_name]
        jpg_original = np.frombuffer(msg_value, np.uint8)
        image = cv2.imdecode(jpg_original, 1)
        return {image_name: image}