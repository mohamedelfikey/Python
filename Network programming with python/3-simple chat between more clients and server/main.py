# client

from socket import *

client = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000

try:
    client.connect((host, port))
    message = ' '
    while message != "exit":
        message = input()
        client.sendall(message.encode())
except error as e:
    print(f"Error: {e}")
finally:
    client.close()
