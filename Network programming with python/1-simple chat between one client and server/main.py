# client
import socket
from socket import *

client = socket(AF_INET, SOCK_STREAM)

host = '127.0.0.1'
port = 7000

try:
    msg = input("")
    client.connect((host, port))
    client.send(msg.encode())
    reply = client.recv(1024)
    print(f"server: {reply.decode('utf-8')}")

except error as e:
    print(f"Error: {e}")

finally:
    client.close()
