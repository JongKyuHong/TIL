import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
# 1

# 11
# 2

# 111
# 12
# 21
# 3

# 1111
# 112
# 121
# 211
# 22
# 13
# 31

# 11111
# 1112
# 1121
# 1211
# 2111
# 113
# 131
# 311
# 221
# 212
# 122
# 32
# 23
for i in range(4, 1000001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009

for _ in range(T):
    N = int(input())
    print(dp[N])
