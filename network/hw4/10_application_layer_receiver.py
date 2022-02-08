import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1119

client_socket.connect((host, port)) #connect to tranport layer.
print("Connected to Transport layer.")


# receive from transport layer of receiver

data = client_socket.recv(1024).decode()

print("Received data from Transport layer.")
print("Received Data is :", data)

client_socket.close()