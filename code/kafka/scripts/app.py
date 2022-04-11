from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from .ui.ui import Ui_MainWindow  

from service.producer import Producer
from service.consumer import Consumer
from service.face_recognition import FaceRecognizer
from service.emotion_classification import EmotionClassificator
from service.data_processing import registrate_user

import configs.config as config

import sys, re, time, json
import cv2 


class Window(QMainWindow):
    _producer = Producer(bootstrap_servers=config.SERVER)
    _file_consumer = Consumer(
        config.FILE_TOPIC, 
        bootstrap_servers=config.SERVER
    )
    _label_consumer = Consumer(
        config.LABEL_TOPIC, 
        bootstrap_servers=config.SERVER,
    )
    _face_recognizer = FaceRecognizer(trained_face_data='./models/haarcascade_frontalface_default.xml')
    _emotion_classificator = EmotionClassificator(model_paths=["./models/modelAugClass1SWFinned.json", "./models/modelAugClass1SWFinned.h5"])
    

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        
    def init_UI(self):
        self.create_menu_bar()
        self.ui.process_button.clicked.connect(self.process_image)

    def create_menu_bar(self):
        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)

        file_menu = QMenu("&File", self)
        self.menuBar.addMenu(file_menu)

        file_menu.addAction("Open", self.action_clicked)
        file_menu.addAction("Save", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            self.fname = QFileDialog.getOpenFileName(self)[0]
            self.load_image()
        elif action.text() == "Save":
            self.save_result()

    def process_image(self):
        try:
            self.fname
        except Exception as e:
            self.not_an_image()
            return
        # start processing
        self.value = self.make_value(path=self.fname)
        self.send_image(self.value) # send 
        if self.take_image(): # take
            self.calculate_result()

    @staticmethod
    def not_an_image():
        error = QMessageBox()
        error.setWindowTitle("Not image")
        error.setText("You must to choose an image!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

        error.exec_()

    @staticmethod
    def not_a_result():
        error = QMessageBox()
        error.setWindowTitle("No result")
        error.setText("You must to process a result before!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

        error.exec_()


    @staticmethod
    def make_value(path: str):
        image = cv2.imread(path)
        retval, buffer = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY),40])
        if not retval:
            print("Error was occurred during image encoding") 
        value = buffer.tobytes()
        # regEx to cut a image name from path
        pattern = re.compile(r'[^\/]+\.(jpg|png)$')
        image_name = pattern.search(path).group()
        return str({image_name: value}).encode()

    @staticmethod
    def send_image(value):
        Window._producer.send(config.FILE_TOPIC, value)
        # time.sleep(2)

    def take_image(self):
        msg = next(Window._file_consumer.kafka_consumer) # get image from consumer
        msg = eval(msg.value.decode())        
        image = Window._file_consumer.poll(msg=msg)
        users = registrate_user(
            img=image, 
            face_recognizer=Window._face_recognizer, 
            emotion_classificator=Window._emotion_classificator)
        users = str(users).encode()
        Window._producer.send(topic=config.LABEL_TOPIC, user=users)
        return True

    def calculate_result(self):
        label = next(Window._label_consumer.kafka_consumer)
        self.result = eval(label.value.decode())

        self.ui.result_text.setPlainText(str(self.result))

    def load_image(self):
        pixmap = QPixmap(self.fname)
        pixmap = pixmap.scaled(560, 380) # resize image
        self.ui.image_label.setPixmap(pixmap)
        # self.ui.image_label.resize(pixmap.width(), pixmap.height())
        # self.resize(pixmap.width(), pixmap.height())

    def save_result(self):
        try:
            self.result 
        except Exception as e:
            self.not_a_result()
            return
        
        fname = QFileDialog.getSaveFileName(self)[0]
        try:
            with open(fname, 'w') as f:
                json.dump(self.result, f, indent=4)
        except Exception as e:
            print(e.__str__())
            print("couldn't save file!")



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()