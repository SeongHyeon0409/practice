import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9999

server_socket.bind((host, port))
server_socket.listen(0)

print("Listening ... ")

client_socket, address = server_socket.accept()

print("Connected to Transport layer.")

while 1:

    data = client_socket.recv(1024).decode()
    print("received : " + data)


client_socket.close()