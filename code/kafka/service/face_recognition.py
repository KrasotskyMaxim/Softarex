import os
import cv2

from .tools import get_images_filenames_from_dir


class FaceRecognizer:
    __pose_counter = 0
    cropped_faces_dir = './cropped-faces/'

    def __init__(self, trained_face_data: str) -> None:
        self.__trained_face_data = cv2.CascadeClassifier(trained_face_data)
        self.__img_crop = []

    def recognize_faces(self, dir_path: str, show_faces: bool = False):
        ''' Extract images from dir and save cropped faces '''
        imgs = get_images_filenames_from_dir(dir_name=dir_path)
        for img_path in imgs:
            img = cv2.imread(img_path)
            face_coordinates = self._get_face_coordinates(img=img)
            self._add_crop_image(img=img, face_coordinates=face_coordinates)

            for counter, cropped in enumerate(self.__img_crop):
                if show_faces:
                    self.show_cropped_face(cropped=cropped)
                self._save_cropped_face(cropped=cropped)
            self.__img_crop = []

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
            self.__img_crop.append(img[y:y + h, x:x + w])

    @staticmethod
    def show_cropped_face(cropped):
        ''' Print shape of cropped image and show cropped face '''
        print(cropped.shape)
        cv2.imshow("Cropped face", cropped)

    def _save_cropped_face(self, cropped, image_format: str = 'png'):
        if not os.path.exists(FaceRecognizer.cropped_faces_dir):
            os.mkdir(FaceRecognizer.cropped_faces_dir)
        cv2.imwrite(FaceRecognizer.cropped_faces_dir+"pose_result_{}.{}".format(FaceRecognizer.__pose_counter, image_format), cropped)
        cv2.waitKey(1)
        FaceRecognizer.__pose_counter += 1



if __name__ == "__main__":
    face_recognizer = FaceRecognizer()
    face_recognizer.recognize_faces(dir_path="face-input/")