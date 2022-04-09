from .producer import Producer
from .consumer import Consumer
from .data_processing import registrate_user
from .face_recognition import FaceRecognizer
from .emotion_classification import EmotionClassificator

import configs.config as config


def main():
    ''' Run a script to get a registed emotions of users '''
    # service
    file_consumer = Consumer(
        config.FILE_TOPIC, 
        bootstrap_servers="127.0.0.1:9095",
    )
    
    producer = Producer(bootstrap_servers=config.SERVER)
    face_recognizer = FaceRecognizer(trained_face_data='./models/haarcascade_frontalface_default.xml')
    emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    
    # run service
    for msg in file_consumer.kafka_consumer:
        msg = eval(msg.value.decode())        
        image = file_consumer.poll(msg=msg)
        users = registrate_user(img=image, face_recognizer=face_recognizer, emotion_classificator=emotion_classificator)
        users = str(users).encode()
        producer.send(topic=config.LABEL_TOPIC, user=users)
    else:
        print("Waiting message...")


if __name__ == "__main__":
    main()