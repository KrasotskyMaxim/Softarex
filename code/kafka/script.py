import producer
from data import registrate_user
from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator

import sys
import glob


def main():
    ''' Run a script to get a registed emotions of users '''
    f = open('log.txt', 'w')
    f.close()
    try:
        working_directory = sys.argv[1]
    except IndexError as ie:
        print("You must to select a working directory!")
        exit()
    
    # service
    face_recognizer = FaceRecognizer(trained_face_data='haarcascade_frontalface_default.xml')
    emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    
    # get images names from directory
    filenames = []
    for image_format in ['jpg', 'png']:
        filenames += glob.glob(working_directory+"*."+image_format)
    filenames.sort()

    # run service
    for filename in filenames:
        print(filename)
        users = registrate_user(img_path=filename, face_recognizer=face_recognizer, emotion_classificator=emotion_classificator)
        producer.send(filename, users)
    


if __name__ == "__main__":
    main()