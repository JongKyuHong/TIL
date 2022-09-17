import sys
import math
input = sys.stdin.readline

#모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현가능
n = int(input())
dp = [50001 for i in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    min_v = sys.maxsize
    j = 1

    while (j**2) <= i:
        min_v = min(min_v, dp[i-(j**2)])
        j += 1
    dp.append(min_v+1)
print(dp[n])

# 자신의 수에서 그보다 작은 수의 제곱수를 뺀것의 최소