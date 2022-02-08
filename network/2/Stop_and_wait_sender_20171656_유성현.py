import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999
ack = 1

client_socket.connect((host, port))
print("Server Connection Successful")

while 1:
    data = input("Send data : ")
    client_socket.send(data.encode())
    timer = int(5)
    flag = 0

    while flag == 0:
        print("Waiting for Ack ...")
        client_socket.settimeout(timer)
        try:
            ack = client_socket.recv(1024).decode()
        except socket.timeout:
            print("Timeout ...")
            print("Resend data ...\n")

            client_socket.send(data.encode())
        else:
            flag = 1

    if flag == 1:
        print("Received Ack", int(ack))
        print('')




