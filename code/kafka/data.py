


def registrate_user(img_path: str, face_recognizer, emotion_classificator):
    # crop faces from images and save it in the directory
    faces = face_recognizer.recognize_faces(img_path=img_path)
    # return an emotions in the cropped faces
    registed = emotion_classificator.classify_emotions(data=faces) 
    return registed 


if __name__ == "__main__":
    pass 