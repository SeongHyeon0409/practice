n = int(input())
blocks = []

blocks.append((0, 0, 0, 0))
for i in range(1, n+1):
    area, height, weight = map(int, input().strip().split()) #넓이 ,높이, 무게
    blocks.append((i, area, height, weight)) #답을 인덱스 별로 출력해야 하기때문에 인덱스 값까지 저장

blocks.sort(key=lambda x:x[3]) # 무게를 기준으로 정렬
dp = [0] * (n+1)


for i in range(1, n+1):
    for j in range(0, i): #무게 별로 정렬해놨기 때문에 더 가벼운 블럭까지만 계산
        if (blocks[j][1] < blocks[i][1]): # 비교할 블록이 현재 블록보다 area가 작을 때
            dp[i] = max(dp[i], dp[j] + blocks[i][2]) #높이를 비교해서 더 높은 높이의 값을 저장

max_height = max(dp)
idx = n
answer = []

#정답 출력
for idx in range(n, 0, -1):
    if max_height == dp[idx]:
        answer.append(blocks[idx][0]) # 가장 아래쪽의 블럭부터 하나씩 꺼내줌
        max_height -= blocks[idx][2] # 나머지 블록들을 꺼내기 위해 꺼낸 블록의 height를 빼줌


print(len(answer))
[print(i) for i in reversed(answer)] #위에있는 블록부터 출력하기 때문에 reversed 사용
