import sys 
input = sys.stdin.readline

n = int(input())
day = [0]
pay = [0]
for _ in range(n):
    t, p = map(int, input().split())
    day.append(t)
    pay.append(p)
dp = [0]*(n+2)

for i in range(1, n+1):
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i + day[i] <= n+1:
        dp[i+day[i]] = max(dp[i+day[i]], dp[i] + pay[i])
    
print(max(dp))