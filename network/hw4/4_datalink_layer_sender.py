import socket, random, time
from bit_stuffing import *
from CSMACD import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1113
ack = 1

client_socket.connect((host, port)) #connect to network layer

print("Connected to Network layer.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1114

server_socket.bind((host, port)) #connect to physical layer.
server_socket.listen(0)

print("Listening ... ")

clientsocket, address = server_socket.accept()

print("Connected to Physical layer.")

#receive from network layer of sender

data = client_socket.recv(1024).decode()

print("Received data from Network layer.")
print("Received Data is :", data)

#bit stuffing

stuffedData = bit_stuff(data)

#send data to datalink layer of sender using CSMA/CD.

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
    clientsocket.send(stuffedData.encode())
    print("Sent the data to physical layer.")
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


###################################################################

#receive ack from physical layer.
print('')

ack = clientsocket.recv(1024).decode()
print("Received ark from Physical layer.")

#bit unstuffing

stuffedAck = bit_unstuff(ack)

#send ack to datalink layer.

client_socket.send(ack.encode())
print("Current ack Status :" , ack)
print("Sent the ack to Network layer.")

client_socket.close()
clientsocket.close()


