import sys
input = sys.stdin.readline


n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        if not dp[i]:
            dp[i] = dp[i-j] + cards[j]
        else:
            dp[i] = min(dp[i], dp[i-j]+cards[j])
print(dp[n])