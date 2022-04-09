import cv2


class FaceRecognizer:
    def __init__(self, trained_face_data: str) -> None:
        self.__trained_face_data = cv2.CascadeClassifier(trained_face_data)
        self.faces = []

    def recognize_faces(self, img, show_faces: bool = False):
        ''' Extract images from dir and return cropped faces '''
        # img = cv2.imread(img_path)
        face_coordinates = self._get_face_coordinates(img=img)
        self._add_crop_image(img=img, face_coordinates=face_coordinates)

        if show_faces:
            for cropped in self.faces:           
                self.show_cropped_face(cropped=cropped)
        
        result = self.faces
        self.faces = []
        return (result, face_coordinates)

    def _get_face_coordinates(self, img):
        ''' Get path to image and detect face coordinates on it '''
        # Must convert to greyscale
        grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect Face
        face_coordinates = self.__trained_face_data.detectMultiScale(grayscaled_img) 
        return face_coordinates

    def _add_crop_image(self, img, face_coordinates):
        ''' Add a cropped faces in the img_crop list '''
        for (x, y, w, h) in face_coordinates:
            self.faces.append(img[y:y + h, x:x + w])

    @staticmethod
    def show_cropped_face(cropped):
        ''' Print shape of cropped image and show cropped face '''
        print(cropped.shape)
        cv2.imshow("Cropped face", cropped)



if __name__ == "__main__":
    face_recognizer = FaceRecognizer()
    face_recognizer.recognize_faces(dir_path="face-input/")