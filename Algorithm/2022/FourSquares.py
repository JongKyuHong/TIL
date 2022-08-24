import sys
import math
input = sys.stdin.readline

#모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현가능
n = int(input())
dp = [50001 for i in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        val = j*j
        print(val)
        if val > i:
            break
        dp[i] = min(dp[i], dp[i-val]+1)

print(dp[n])