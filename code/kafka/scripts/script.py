from kafka import KafkaProducer
import glob, time, json
import cv2
import configs.config as config

kafka_producer = KafkaProducer(
    bootstrap_servers=config.SERVER,
    # value_serializer=lambda m: json.dumps(m).encode()
    )
DIR = './face-input/'
filenames, index = [], 0


def check_new_filenames():
    global filenames
    for image_format in ['jpg', 'png']:
        images_list = glob.glob(DIR+"*."+image_format)
        filenames += [x for x in images_list if x not in filenames]
    # print(filenames)

def make_value(path: str):
    image = cv2.imread(path)
    retval, buffer = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY),40])
    if not retval:
        print("Error was occurred during image encoding") 
    value = buffer.tobytes()
    return str({path: value}).encode()


if __name__ == "__main__":
    while True:
        check_new_filenames()
        try:
            filenames[index]
        except IndexError as ie:
            print("Waiting new images...")
            time.sleep(3)
            continue
        path = filenames[index]
        print(path)
        value = make_value(path=path)
        kafka_producer.send(config.FILE_TOPIC, value)
        time.sleep(2)
        index += 1