

def registrate_user(img: str, face_recognizer, emotion_classificator):
    # crop faces from images and save it in the directory
    faces, coordinates = face_recognizer.recognize_faces(img=img)
    # return an emotions in the cropped faces
    registed = emotion_classificator.classify_emotions(data=faces)

    result = [] # return

    for t, l in zip(coordinates, registed):
        coords = {} # x, y, width, height
        box_and_labels = {} # box, label
        coords['x'], coords['y'], coords['width'], coords['height'] = int(t[0]), int(t[1]), int(t[2]), int(t[3])
        box_and_labels["box"], box_and_labels["label"] = coords, l 
        result.append(box_and_labels)
        
    # print(result)
    return result