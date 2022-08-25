import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (k+1)

max_v = 0
cnt = 0
flag = 0
for i in range(n):
    if nums[i] % 2 == 0:
        flag = 1
        cnt += 1
    else:
        if flag:
            if max_v < cnt:
                max_v = cnt
                k -= 1
                dp[k] = max(max_v, dp[k])
        cnt = 0
        flag = 0
print(dp[k])
            
            
