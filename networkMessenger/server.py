import socket, threading


def register(username, password):
    user, addrSocket = s.accept()
    if user not in person :
        user.sendall("this username registered")
    user.sendall("you registered successfully")


class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        listuer = [self.username]


person = User()
port = 1234
host = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(20)
while True:
    commandString = str(s.recv(2048))
    commandString = commandString.split(' ')
    command = commandString[0]
    if command == "register":
        register(command[1], command[2])
