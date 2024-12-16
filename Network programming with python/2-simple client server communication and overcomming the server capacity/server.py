# server
from socket import *

server = socket(AF_INET, SOCK_STREAM)

address = ('127.0.0.1', 6000)
length = 50

server.bind(address)
server.listen()
c, addr = server.accept()
message = b''

while True:
    chunk = c.recv(length)
    if not chunk:
        break
    message += chunk

if message:
    print(message.decode('utf-8'))
    c.close()
