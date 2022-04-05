from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator


def get_emotion_labels(img_path: str):
    face_recognizer = FaceRecognizer(trained_face_data='haarcascade_frontalface_default.xml')
    # crop faces from images and save it in the directory
    faces = face_recognizer.recognize_faces(dir_path=img_path)

    emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    # return an emotions in the cropped faces
    result = emotion_classificator.classify_emotions(data=faces) 
    return result



if __name__ == "__main__":
    print(get_emotion_labels())