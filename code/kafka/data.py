


def registrate_user(img_path: str, face_recognizer, emotion_classificator):
    # crop faces from images and save it in the directory
    faces, coordinates = face_recognizer.recognize_faces(img_path=img_path)
    # return an emotions in the cropped faces
    registed = emotion_classificator.classify_emotions(data=faces)

    result = [] # return

    for t, l in zip(coordinates, registed):
        coords = {} # x, y, width, height
        box_and_labels = {} # box, label
        # print(t[0], t[1], t[2], t[3])
        # print(l)
        coords['x'], coords['y'], coords['width'], coords['height'] = int(t[0]), int(t[1]), int(t[2]), int(t[3])
        # print(coords)
        box_and_labels["box"], box_and_labels["label"] = coords, l 
        # print(box_and_labels)
        result.append(box_and_labels)
    print(result)
    return result



if __name__ == "__main__":
    pass 