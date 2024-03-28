n = int(input())
g = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = g[0]

if n > 1:
    dp[1] = g[0] + g[1]

if n > 2:
    dp[2] = max(dp[1], g[1]+g[2] ,g[0]+g[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + g[i], dp[i-1], dp[i-3]+g[i-1]+g[i])

print(dp)
print(dp[-1])

#-----------

n = int(input())
gr = []
for i in range(n):
    gr.append(int(input()))

gr.extend([0,0])
    # 연속으로 3번 X

    # 자기거 x 전에거
    # 전전거 + 자기거
    # 자기거 전거 + 전전전거

dp = [0] * (n + 2)
dp[0] = gr[0]
dp[1] = gr[0] + gr[1]
dp[2] = max(dp[1], gr[1] + gr[2], gr[0] + gr[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + gr[i], dp[i-3] + gr[i-1] + gr[i])

print(dp[n-1])

