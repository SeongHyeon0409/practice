import socket
from multi_transition import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1114
ack = 1

client_socket.connect((host, port)) #connect to datalink layer.

print("Connected to Datalink layer.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1115

server_socket.bind((host, port)) #connect to physical layer of receiver.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Physical layer of Receiver.")

#receive from datalink layer of sender.

data = client_socket.recv(1024).decode()

print("Received data from datalink layer.")
print("Received Data is :", data)

#Multi transition MLT 3 scheme

data = multi_transition(data)


#send data to physical layer of receiver.

clientsocket.send(data.encode())
print("Sent the data to Physical layer of Receiver.")


###################################################################

#receive ack from physical layer of receiver.
print('')

rack = clientsocket.recv(1024).decode()
print("Received ark from Datalink layer.")

#Reverse MLT 3 scheme

ack = r_multi_transition(rack)

#send the ack to physical layer.

client_socket.send(ack.encode())
print("Current ack Status :" , ack)
print("Sent the ack to Physical layer of Sender.")

client_socket.close()
clientsocket.close()




