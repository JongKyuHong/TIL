import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[] for i in range(n+1)]
dp[0] = [s]

for i in range(n):
    ans = set()
    for j in dp[i]:
        if j+v[i] <= m:
            ans.add(j + v[i])
        if j-v[i] >= 0:
            ans.add(j-v[i])
    dp[i+1].extend(list(ans))

print(max(dp[n]) if dp[n] else -1)