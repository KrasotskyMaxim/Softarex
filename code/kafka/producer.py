import json
import os


class Producer:
    def __init__(self, to_save: str = 'log.json') -> None:
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