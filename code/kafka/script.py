from kafka import KafkaProducer
import config
import glob, time, json


producer = KafkaProducer(
    bootstrap_servers=config.SERVER,
    value_serializer=lambda m: json.dumps(m).encode()
    )
DIR = 'face-input/'
filenames, index = [], 0


def check_new_filenames():
    global filenames
    for image_format in ['jpg', 'png']:
        images_list = glob.glob(DIR+"*."+image_format)
        filenames += [x for x in images_list if x not in filenames]
    # print(filenames)


if __name__ == "__main__":
    while True:
        check_new_filenames()
        try:
            filenames[index]
        except IndexError as ie:
            print("Waiting new images...")
            time.sleep(3)
            continue
        producer.send(config.FILE_TOPIC, filenames[index])
        print(filenames[index])
        time.sleep(2)
        index += 1