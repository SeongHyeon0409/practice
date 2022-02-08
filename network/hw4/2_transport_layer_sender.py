import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1111
ack = 1

client_socket.connect((host, port)) #connect to application layer.

print("Connected to Application layer.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1112

server_socket.bind((host, port)) #connect to network layer.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Network layer.")

#receive from application layer of sender.

data = client_socket.recv(1024).decode()

print("Received data from application layer.")
print("Received Data is :", data)

#send data to network layer of sender using stop and wait protocol.

timer = 10
flag = 0

while flag == 0:
    clientsocket.send(data.encode())
    print("Sent the data to network layer.")

    ###################################################################
    # receive ack from network layer.
    print("")
    print("Waiting for Ack ...")
    clientsocket.settimeout(timer)
    try:
        ack = clientsocket.recv(1024).decode()
    except socket.timeout:
        print("Timeout ...")
        print("Resend data ...\n")

    else:
        flag = 1

if flag == 1:
    print("Received Ack form Network layer.")

    # send ack to datalink layer.

    client_socket.send(ack.encode())
    print("Current ack Status :" , ack)
    print("Sent the ack to Application layer.")


client_socket.close()
clientsocket.close()




