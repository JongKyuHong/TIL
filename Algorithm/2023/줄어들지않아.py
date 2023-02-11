import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*64
dp[0] = 10
dp[1] = 55
ten = [i for i in range(1, 11)]
idx = 2
tmp = [dp[idx-1]]
while idx < 64:
    target = dp[idx-1]
    for i in range(9,0,-1):
        tmp.append(target-ten[i])
        target -= ten[i]
    dp[idx] = (sum(tmp))
    tmp.reverse()
    ten = tmp[:]
    idx += 1
    tmp = [dp[idx-1]]
    
for _ in range(T):
    n = int(input())
    print(dp[n-1])
