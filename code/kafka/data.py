from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator


def get_emotion_labels(dir_path: str = "face-input/"):
    face_recognizer = FaceRecognizer()
    # crop faces from images and save it in the directory
    face_recognizer.recognize_faces(dir_path=dir_path)

    emotion_classificator = EmotionClassificator()
    # return an emotions in the cropped faces
    result = emotion_classificator.classify_emotions("cropped-faces/") 
    return result



if __name__ == "__main__":
    print(get_emotion_labels())