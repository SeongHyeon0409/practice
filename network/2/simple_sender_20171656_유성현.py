import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999

client_socket.connect((host, port))
print("Server Connection Successful")
while 1:
    r = input("Send data : ")
    client_socket.send(r.encode())




