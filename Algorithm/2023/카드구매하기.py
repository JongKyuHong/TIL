import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1, N+1):
    for j in range(1, N+1):
        if not dp[i]:
            dp[i] = dp[i-j] + lst[j]
        else:
            dp[i] = min(dp[i], dp[i-j]+lst[j])
print(dp[N])