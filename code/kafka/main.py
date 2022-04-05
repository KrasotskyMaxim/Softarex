from numpy import product
from producer import Producer
from consumer import Consumer
from data import registrate_user
from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator

import sys
import time


def main():
    ''' Run a script to get a registed emotions of users '''
    try:
        working_directory = sys.argv[1]
    except IndexError as ie:
        print("You must to select a working directory!")
        exit()
    
    # service
    consumer = Consumer(working_directory=working_directory)
    producer = Producer()
    face_recognizer = FaceRecognizer(trained_face_data='haarcascade_frontalface_default.xml')
    emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    
    # # run service
    while True:
        image = consumer.poll()
        print(image)
        if not image:
            print("Waiting new images...")
            time.sleep(2)
            continue
        users = registrate_user(img_path=image, face_recognizer=face_recognizer, emotion_classificator=emotion_classificator)
        producer.send(users)
    


if __name__ == "__main__":
    main()