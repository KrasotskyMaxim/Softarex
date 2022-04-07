import json
from kafka import KafkaProducer


class Producer(KafkaProducer):
    def __init__(self, to_save: str = 'log.json', bootstrap_servers: str = "127.0.0.1:9095") -> None:
        super().__init__(bootstrap_servers=bootstrap_servers)
        self.to_save = to_save
        f = open(self.to_save, 'w')
        f.close()

    def send(self, user) -> list:
        ''' Return an emotions of registed users '''
        try:
            with open(self.to_save, 'a') as f:
                json.dump(user, f, indent=4)
            print("Log write in file!")
        except Exception as e:
            print(e.__str__())
    

if __name__ == "__main__":
    pass 