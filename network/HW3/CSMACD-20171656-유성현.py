import time
import random

statistics = []
limit = 0
k = 0
success = False
abort = False
collisionChance = 5 # collision이 일어날 확률

def simulate():

    global limit, k, data, collisionChance
    global success, abort

    limit = int(input("Enter the maximum number of attemps : "))

    while (success != True and abort != True):
        attempt()

    if abort == True:
        k -= 1

    time.sleep(1)
    output()


def attempt():

    global limit, k, data, collisionChance
    global success, abort
    global statistics

    Tb = 2 #Back-off time
    Channelbusy = 0

    print("\nAttemp ", k + 1, ":")

    while Channelbusy == 0:
        print("The channel is busy ... ")  #1-Persistent Methods
        Channelbusy = random.randint(0,1)
        time.sleep(1)

    print("The channel is idle, Station can transmit ... ")
    time.sleep(1)

    if collisionChance > random.randint(0, 9): #collision이 발생할 확률
        statistics.append("Failed")
        print("A conflict has occurred ... ")
    else:
        print("Acknowledgement was received. The attemp was successful.")
        success = True
        statistics.append("Successful")
    time.sleep(1)


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
        time.sleep(1)

def chooseR(k):
    r = random.randint(0, 2 ** k - 1)
    return r

def output():
    print("\n")
    for i in range(0, k + 1):
        print ("Attemp ",i + 1, " : ",statistics[i])

if __name__ == "__main__":
    simulate()