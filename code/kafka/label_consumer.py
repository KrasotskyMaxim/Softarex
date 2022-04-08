from consumer import Consumer
import config, time


label_consumer = Consumer(
        config.LABEL_TOPIC, 
        bootstrap_servers="127.0.0.1:9095",
        working_directory=None,
    )

print("Start label consumer!")

for label in label_consumer.kafka_consumer:
    print(label.value.decode())
    time.sleep(1)