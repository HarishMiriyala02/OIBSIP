import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input("")
            client_socket.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error sending message: {e}")
            break

HOST = '127.0.0.1'
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()
