# client
from socket import *

client = socket(AF_INET, SOCK_STREAM)

address = ('127.0.0.1', 6000)

try:
    client.connect(address)
    message = 'Hello from client: my name is Mohamed Ahmed I\'m a CSE and bla bla bla'
    # this entire message can't be send because the size capacity of server but we can handle it

    client.sendall(message.encode('utf-8'))

except error as e:
    print(f"message error {e}")

finally:
    client.close()
