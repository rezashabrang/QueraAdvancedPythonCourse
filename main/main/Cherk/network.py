import socket, threading

def threaded(c, addr):
    while True:
        data = c.recv(1024)
        if data == 'exit':
            print('Conncetion to', addr[0], ':', addr[1], 'lost.')
            break

        data = data[::-1]
        c.sendall(data)

    c.close()


host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print('socket binded to post', port)

s.listen(10)
print('socket is listening...')

for i in range(10):
    c, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])
    threading.Thread(target=threaded, args=(c,addr)).start()

s.close()