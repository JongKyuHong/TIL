import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

path = []
max_v = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == max_v:
        path.append(lst[i])
        max_v -= 1
path.reverse()
print(*path)
