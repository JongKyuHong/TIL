INF = float('inf')
n = int(input())
a = list(map(int, input().split()))

dp = [0] + [INF] * (n-1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i-j)*(1+abs(a[i]-a[j])),dp[j])
        dp[i] = min(dp[i],power)
print(dp[-1])