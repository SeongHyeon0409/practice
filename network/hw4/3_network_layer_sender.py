import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1112
ack = 1

client_socket.connect((host, port)) #connect to transprot layer

print("Connected to Transport layer.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1113

server_socket.bind((host, port)) #connect to datalink layer.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Datalink layer.")

#receive from transport layer of sender

data = client_socket.recv(1024).decode()

print("Received data from transport layer.")
print("Received Data is :", data)

#send data to datalink layer of sender.

clientsocket.send(data.encode())
print("Sent the data to datalink layer.")

###################################################################

#receive ack from datalink layer.
print('')

ack = clientsocket.recv(1024).decode()
print("Received ark from datalink layer.")

#send ack to transport layer.

client_socket.send(ack.encode())
print("Current ack Status :", ack)
print("Sent the ack to Transport layer.")

client_socket.close()
clientsocket.close()



