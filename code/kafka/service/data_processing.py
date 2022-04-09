

def registrate_user(img: str, face_recognizer, emotion_classificator):
    # crop faces from images and save it in the directory
    image_name = list(img.keys())[0]
    image = img[image_name]
    faces, coordinates = face_recognizer.recognize_faces(img=image)
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
    return {image_name: result}