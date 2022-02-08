import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1117
ack = 1

client_socket.connect((host, port)) #connect to datalink layer of receiver.

print("Connected to Datalink layer of Sender.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1118

server_socket.bind((host, port)) #connect to transport layer of receiver.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Transport layer.")

#receive from datalink layer.

data = client_socket.recv(1024).decode()

print("Received data from Datalink layer.")
print("Received Data is :", data)

#send data to transport layer.

clientsocket.send(data.encode())
print("Sent the data to Transport layer.")

###################################################################

#receive ack from transport layer.
print('')

ack = clientsocket.recv(1024).decode()
print("Received ark from Transport layer.")

#send ack to datalink layer.

client_socket.send(ack.encode())
print("Current ack Status :" , ack)
print("Sent the ack to Datalink layer.")

client_socket.close()
clientsocket.close()