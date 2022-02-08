import socket
from multi_transition import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1115
ack = 1

client_socket.connect((host, port)) #connect to physical layer of sender.

print("Connected to Physical layer of Sender.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1116

server_socket.bind((host, port)) #connect to datalink layer of receiver.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Datalink layer.")

#receive from physical layer of sender.

data = client_socket.recv(1024).decode()

print("Received data from Physical layer of sender.")
print("Received Data is :", data)

#Reverse MLT 3 scheme

data = r_multi_transition(data)

#send data to datalink layer.

clientsocket.send(data.encode())
print("Sent the data to Datalink layer.")


###################################################################

#receive ack from datalink layer.
print('')

ack = clientsocket.recv(1024).decode()

print("Received ark from Datalink layer.")

#Multi transition MLT 3 scheme

ack = multi_transition(ack)

#send the ack to physical layer.

client_socket.send(ack.encode())
print("Current ack Status :" , ack)
print("Sent the ack to Physical layer.")

client_socket.close()
clientsocket.close()


