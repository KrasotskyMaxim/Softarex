from producer import Producer
from consumer import Consumer
from data import registrate_user
from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator

import sys, time
import config


def main():
    ''' Run a script to get a registed emotions of users '''
    # try:
    #     working_directory = sys.argv[1]
    # except IndexError as ie:
    #     print("You must to select a working directory!")
    #     exit()
    
    # service
    consumer = Consumer(
        config.FILE_TOPIC, 
        config.LABEL_TOPIC, 
        bootstrap_servers="127.0.0.1:9095",
        working_directory=None,
    )
    # consumer = Consumer(topic=config.TOPIC, bootstrap_servers=config.SERVER, working_directory=working_directory)
    producer = Producer(bootstrap_servers=config.SERVER)
    face_recognizer = FaceRecognizer(trained_face_data='./models/haarcascade_frontalface_default.xml')
    emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    
    # run service
    for msg in consumer.kafka_consumer:        
        image = consumer.poll(msg=msg)
        # print(image)
        # if isinstance(image, bool):
        #     print("Waiting new images...")
        #     time.sleep(2)
        #     continue
        users = registrate_user(img=image, face_recognizer=face_recognizer, emotion_classificator=emotion_classificator)
        # producer.send(topic=config.LABEL_TOPIC, user=users)
    else:
        print("Waiting message...")


if __name__ == "__main__":
    main()