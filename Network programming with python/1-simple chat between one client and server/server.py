# server
from socket import *

s = socket(AF_INET, SOCK_STREAM)

host = '127.0.0.1'
port = 7000

s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    msg = c.recv(1024)
    if msg:
        print(f"from client: {msg.decode('utf-8')}")
        reply = input()
        c.sendall(reply.encode())
