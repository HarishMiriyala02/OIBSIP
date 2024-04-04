import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                print(f"Connection from {client_address} closed.")
                break
            print(f"Received from {client_address}: {message}")
            broadcast_message(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

HOST = '127.0.0.1'
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server is listening...")

clients = []

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
