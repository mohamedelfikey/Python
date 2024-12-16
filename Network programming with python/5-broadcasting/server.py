import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 7070
clients = []


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break


def receive_connections():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()


# Setting up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on {HOST}:{PORT}")
receive_connections()
