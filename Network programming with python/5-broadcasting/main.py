import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 7070


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("Connection closed by the server.")
            client.close()
            break


def send_messages(client):
    while True:
        message = input('')
        client.send(message.encode('utf-8'))


# Setting up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Starting threads to handle sending and receiving messages
threading.Thread(target=receive_messages, args=(client,)).start()
threading.Thread(target=send_messages, args=(client,)).start()
