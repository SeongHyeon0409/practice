def solution(bandage, health, attacks):
    last_time = attacks[-1][0]
    full_hp = health
    continuity = 0
    heat = False

    for time in range(last_time+1):
        for time1, damage in attacks:
            if time == time1:
                health -= damage
                continuity = 0
                heat = True
                if health < 1:
                    return -1
        if heat == False:
            health += bandage[1]
            continuity += 1
        if continuity == bandage[0]:
            health += bandage[2]
            continuity = 0
        if health >= full_hp:
            health = full_hp
        heat = False
        print(time, health)
    return health