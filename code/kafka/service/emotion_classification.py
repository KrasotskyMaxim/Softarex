from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy as np
import cv2


class EmotionClassificator:
    __emotions = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

    def __init__(self, model_paths: list) -> None:
        self.model = EmotionClassificator._load_model(model_path=model_paths[0], weights_path=model_paths[1])
        self.predict_dataset = [] # store images for predict

    def classify_emotions(self, data):
        ''' Answer what emotion a faces contains '''
        # cropped = get_images_filenames_from_dir(dir_name=dir_path, image_format='png')
        cropped = data 
        # fill predict dataset
        for f in cropped:
            np_image = self.convert_image(f)
            self.predict_dataset.append(np_image)
        self.normalize_predict_dataset()
        # create data for predict
        X_predict = self.reshape_dataset(self.predict_dataset)
        results = self.predict_emotions(X=X_predict)
        emotion_classification = self.make_final_predict(results=results, X_predict=X_predict)
        self.predict_dataset = []
        return emotion_classification

    def predict_emotions(self, X):
        ''' Return a prediction results '''
        return self.model.predict(x=X)

    @staticmethod
    def _load_model(model_path, weights_path):
        ''' Load pre-trained model and wights from paths '''
        # load json and create model
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights(weights_path)
        print("Loaded model from disk\n")
        return model

    def convert_image(self, img, show_image: bool = False):
        ''' Resize image into size 48x48, convert into numpy array and return it '''
        # image = Image.open(img)
        # resized_image = image.resize((48, 48))
        np_image = cv2.resize(img, dsize=(48, 48), interpolation=cv2.INTER_CUBIC)
        # np_image = np.asarray(resized_image)
        if show_image:
            EmotionClassificator._show_converted_image(np_image)
        return np_image

    def normalize_predict_dataset(self):
        ''' Normalize all images in the predict dataset '''
        for i in range(len(self.predict_dataset)):
            r = cv2.normalize(self.predict_dataset[i], None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            self.predict_dataset[i] = r

    @staticmethod
    def reshape_dataset(data, show_shape: bool = False):
        ''' Return a reshaped dataset '''
        new_data = np.reshape(data,(len(data), 48,48,3))
        if show_shape:
            print(new_data.shape)
        return new_data

    @staticmethod
    def _show_converted_image(image):
        ''' Show an image, it`s mode and shape '''
        print(image.shape)
        plt.imshow(image, interpolation='nearest')
        plt.show()

    def make_final_predict(self, results, X_predict, show_labels_and_images: bool = False):
        ''' Return a final predict labels list '''
        final_predict = []
        label = None
        show_cnt = 0
        for r, img in zip(results, X_predict):
            emotion_number = list(r).index(max(r))
            label = EmotionClassificator.__emotions[emotion_number]
            if show_labels_and_images:
                plt.title(label=label)
                plt.imshow(self.predict_dataset[show_cnt], interpolation='nearest')
                plt.show()
                show_cnt += 1
            final_predict.append((img, label))
        return final_predict


if __name__ == "__main__":
    emotion_classificator = EmotionClassificator()
    result = emotion_classificator.classify_emotions("cropped-faces/") 
    print(result)