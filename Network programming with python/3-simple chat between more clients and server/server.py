from socket import *
from threading import Thread

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.bind((host, port))


def client_server(c, addr):
    data = " "
    while data != 'exit':
        data = c.recv(1024)
        if data:
            print(f"{addr[1]}: {data.decode('utf-8')} ")


while True:
    s.listen()
    c, addr = s.accept()
    thread = Thread(target=client_server, args=(c, addr))
    thread.start()
