import json
import bcrypt
import sys
import time

salt = bcrypt.gensalt(14)

data = {}


class user():
    def __init__(self):
        self.user = ""
        self.passw = ""
        self.decider = ""
        self.userTaken = True  # Just set to true for checking if username is taken

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
        try:
            authenticated = bcrypt.checkpw(self.passw.encode(), data[self.user.lower()]["password"].encode())
        except KeyError:
            print("Access Denied")
            sys.exit()

        if authenticated:
            print("Access Granted")
        else:
            print("Access Denied")

    def register(self):
        global data
        self.user = input("Please enter your desired username: ")
        self.passw = input("Please enter your desired password: ")
        if self.user in data:
            print("I'm sorry but the username you entered is taken \nPlease pick a new username")
            time.sleep(1.5)
            self.Main()
        else:
            print("Account has been created!")
            self.createAccount(self.user, self.passw)

    def createAccount(self, username, password):
        password = bcrypt.hashpw(password.encode(), salt)
        password = str(password)
        #password = password[:-1]
        password = password[2: -1:]
        userDetails = {username.lower(): {"password": str(password)}}
        data.update(userDetails)
        self.updateData(data)

    def updateData(self, fileContents):
        with open('data.json', "w") as file:
            json.dump(fileContents, file)


user = user()

user.Main()