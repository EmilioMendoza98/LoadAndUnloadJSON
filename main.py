import json
import bcrypt
import sys

salt = bcrypt.gensalt(14)

data = {}


class user():
    def __init__(self):
        self.user = None
        self.passw = None
        self.decider = None

    def loadDB(self):
        global data
        fileName = "data.json"
        with open(fileName) as f:
            data = json.load(f)

    def Main(self):
        self.loadDB()
        self.decider = input("Do you want to login or register (1:2): ")
        if self.decider == "1":
            self.login()
        elif self.decider == "2":
            self.register()
        else:
            sys.exit()

    def login(self):
        self.loadDB()
        self.user = input("What is your username: ")
        self.passw = input("What is your password: ")
        authenticated = bcrypt.checkpw(self.passw.encode(), data["Ironislife98"]["password"].encode())
        if authenticated:
            print("Access Granted")
        else:
            print("Access Denied")



    def register(self):
        pass


user = user()

user.Main()