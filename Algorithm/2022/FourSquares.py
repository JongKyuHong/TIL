import sys
import math
input = sys.stdin.readline

#모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현가능
n = int(input())
dp = [float('inf')]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    j = 1
    while (j**2) <= i:
        dp[i] = min(dp[i], dp[i-(j**2)]+1)
        j += 1
print(dp[n])