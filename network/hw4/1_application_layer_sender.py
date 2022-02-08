import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1111

server_socket.bind((host, port)) #connect to tranport layer.
server_socket.listen(0)

print("Listening ... ")

client_socket, address = server_socket.accept()

print("Connected to Transport layer.")

#send data to transport layer of sender.

data = input("Send data (ex 10010001) : ")
data = data.replace(" ", "")

bit_ary = list(data)


try:
    bit_ary = [int(i) for i in bit_ary]
except:
    print("숫자만 입력하세요.")
    exit()

for i in bit_ary:
    if i != 1 and i != 0:
        print("1과 0 만입력하세요")
        exit()

client_socket.send(str(data).encode())
print("Sent the data to transport layer.")

###################################################################

#receive ack from transport layer.
print('')

ack = client_socket.recv(1024).decode()
print("Received ack from Transport layer.")
print("Received for outgoing message.") #end scenario


client_socket.close()




