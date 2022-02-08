def solution(genres, plays):
    answer = []
    playsum = {}
    for i in range(len(genres)):
        if genres[i] not in playsum:
            playsum[genres[i]] = plays[i]
        else:
            playsum[genres[i]] += plays[i]

    playdic = []
    for i in range(len(genres)):
        a = genres[i]
        b = plays[i]
        playdic.append([a, b])

    playsum = sorted(playsum.items(), key=lambda x: x[1], reverse=True)

    for i in playsum:  # classic, pop
        count = 0
        while count < 2:
            maxv = 0
            idx = -1
            for j in range(len(playdic)):
                if playdic[j][0] == i[0] and playdic[j][1] > maxv:
                    print(playdic[j])
                    maxv = playdic[j][1]
                    idx = j

            if idx > -1:
                answer.append(idx)
                playdic[idx][1] = 0
                playdic[idx][0] = 0

            count += 1

    return answer

print(solution(['A', 'B', 'A', 'A', 'B'], [
      500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B'], [500]) == [0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
