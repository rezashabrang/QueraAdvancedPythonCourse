import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = None
        self.dead = False

    def start(self):
        self.s.connect(self.host, self.port)
        configfile = open("config.json", "wb")
        configfile.write(self.s.recv(2048))
        configfile.close()
        configfile = open("config.json")
        jsonRead = json.load(configfile.read())
        configfile.close()
        self.id = jsonRead["id"]


    def send_data(self, keys):

        if keys==[]:
            self.s.sendall(str(json.dumps({"keys":["sanke_"+str(self.id)+"_no_key"],"dead":False})).encode("ascii"))
        else:
            self.s.sendall(str(json.dumps({"keys": ["snake_"+str(self.id)+"_"+keys[0]], "dead": False})).encode("ascii"))


    def get_data(self):

        SSS=''
        aaa=self.s.recv(2048).decode("ascii")
        for char in aaa:
            if char=="'":
                SSS+='"'
            else:
                SSS+=char
        return json.loads(SSS)
