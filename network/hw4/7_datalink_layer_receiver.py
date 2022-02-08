import socket,random, time
from bit_stuffing import *
from CSMACD import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1116
ack = 1

client_socket.connect((host, port)) #connect to physical layer.

print("Connected to Physical layer.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1117

server_socket.bind((host, port)) #connect to network layer.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Network layer.")

#receive from physical layer.

data = client_socket.recv(1024).decode()

print("Received data from Physical layer.")
print("Received Data is :", data)

#bit unstuffing

stuffedData = bit_unstuff(data)

#send data to physical layer of receiver.

clientsocket.send(stuffedData.encode())
print("Sent the data to Physical layer of Receiver.")


###################################################################

#receive ack from transport layer.
print('')

ack = clientsocket.recv(1024).decode()
print("Received ack from Network layer.")

#bit stuffing

stuffedAck = bit_stuff(ack)

#send ack to datalink layer using CSMA/CD.

collisionChance = 0 # collision이 일어날 확률
statistics = []
limit = 0
k = 0
success = False
abort = False

Tb = 2 #Back-off time
Channelbusy = 0

while Channelbusy == 0:
    print("The channel is busy ... ")  #1-Persistent Methods
    Channelbusy = random.randint(0,1)
    time.sleep(1)

print("The channel is idle, Station can transmit ... ")
time.sleep(1)

if collisionChance > random.randint(0, 10): #collision이 발생할 확률
    statistics.append("Failed")
    print("A conflict has occurred ... ")
else:
    client_socket.send(stuffedAck.encode())
    print("Current ack Status :", ack)
    print("Sent the ack to Physical layer.")
    success = True
    statistics.append("Successful")

if success == False:
    print("Send a jamming signal ...")
    time.sleep(1)
    k += 1
    if k < limit:
        Tbtime = Tb * 0.1 * chooseR(k)  # wait Tb time (maxtimum propagation time * R)
        print("Waiting the TB timer to expire and to start a new attemp ... : ",Tbtime)
        time.sleep(1 + Tbtime)

    else:
        print("The whole process was aborted. We need to try another time.")
        abort = True

client_socket.close()
clientsocket.close()
