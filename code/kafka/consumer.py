import glob, config
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
        
    # def check_new_images(self):
    #     for image_format in ['jpg', 'png']:
    #         images_list = glob.glob(self.working_directory+"*."+image_format)
    #         self.filenames += [x for x in images_list if x not in self.filenames]

    def poll(self, msg: str):
        ''' Send a converted image to classificator '''
        jpg_original = np.frombuffer(msg.value, np.uint8)
        image = cv2.imdecode(jpg_original, 1)
        return image

        # self.check_new_images() 
        # try:
        #     self.filenames[self.index]
        # except IndexError as ie:
        #     return False 
        # index = self.index
        # self.index += 1
        # print(self.filenames[index])
        # return cv2.imread(self.filenames[index])
        
            
    
if __name__ == "__main__":
    consumer = Consumer(
        config.FILE_TOPIC, 
        config.LABEL_TOPIC, 
        bootstrap_servers="127.0.0.1:9095",
    )

    for msg in consumer.kafka_consumer:
        # img_path = msg.value.decode()
        # print(img_path)
        consumer.poll(msg=msg)