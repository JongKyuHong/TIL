import sys 
input = sys.stdin.readline

N = int(input())
brick = []
brick.append((0, 0, 0, 0))
for idx in range(1,N+1):
    width, height, weight = map(int, input().split())
    brick.append((idx, width, height, weight))

brick.sort(key=lambda x: x[3])
dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(0, i):
        if brick[i][1] > brick[j][1]:
            dp[i] = max(dp[i], dp[j] + brick[i][2])

max_v = max(dp)
index = N
result = []
while index != 0:
    if max_v == dp[idx]:
        result.append(brick[idx][0])
        max_v -= brick[idx][2]
    index -= 1
result.reverse()
print(len(result))
[print(i) for i in result]
