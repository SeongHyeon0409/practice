import socket
from random import *
from time import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9999
ack = 0
s_data = ''

server_socket.bind((host, port))
server_socket.listen(0)

print("Listening ... ")

client_socket, address = server_socket.accept()

print("accepting .")

while 1:
    data = client_socket.recv(1024).decode()
    if data != s_data: #같은 데이터가 다시 들어오면 보냈던 ack를 다시 보냄
        ack = 1 if ack == 0 else ack == 0

    print("received :", data)
    s_data = data

    random = randrange(0, 10)
    if random < 7: #70% 확률로 ack를 보냄
        client_socket.send(str(int(ack)).encode()) # send ack
        print("Send a ack", int(ack))
    else:
        print("Failed to send ack ...")

    print('')

client_socket.close()