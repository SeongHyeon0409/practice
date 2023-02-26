record = []
point = [10, 8, 6, 5, 4, 3, 2, 1]
for i in range(8):
    time, team = input().split()
    time = time.replace(":", "")
    record.append([int(time), team])
redp = 0
bluep = 0
record.sort()
for i, team in enumerate(record):
    if team[1] == "R":
        redp += point[i]
    else:
        bluep += point[i]

print("Red" if redp > bluep else "Blue")

