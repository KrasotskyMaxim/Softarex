import producer
import sys

def main():
    ''' Run a script to get a registed emotions of users '''
    try:
        users = producer.start_registed_users(path=sys.argv[1])
        print(users)
    except IndexError as ie:
        print("You must to select a working directory!")


if __name__ == "__main__":
    main()