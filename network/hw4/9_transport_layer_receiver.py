import socket
from random import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1118
ack = 1

client_socket.connect((host, port)) #connect to network layer of receiver.

print("Connected to Datalink layer of Sender.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1119

server_socket.bind((host, port)) #connect to application layer of receiver.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Transport layer.")

s_data = ''

#receive from network layer.

data = client_socket.recv(1024).decode()

print("Received data from Network layer.")
print("Received Data is :", data)

# send data to application layer.

clientsocket.send(data.encode())
print("Sent the data to Application layer.")

###################################################################

# send back ACK to network layer.
print('')

if data != s_data: #같은 데이터가 다시 들어오면 보냈던 ack를 다시 보냄
    ack = 1 if ack == 0 else ack == 0

s_data = data

ack = '010000010101001001001011' #ASCII code

random = randrange(0, 10)
if random < 10: #100% 확률로 ack를 보냄
    client_socket.send(ack.encode()) # send ack
    print("Current ack Status :", ack)
    print("Send a ack to Network layer.")
else:
    print("Failed to send ack ...")


client_socket.close()
clientsocket.close()





