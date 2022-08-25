import sys
input = sys.stdin.readline

while 1:
    n = int(input()) # 창업한지 n일
    if n == 0:
        break
    # 가장 돈을 많이 번 구간
    cost = [int(input()) for _ in range(n)]
    max_v = -10001
    dp[0] = max(max_v,cost[0])
    for i in range(1,n):
        if cost[i] + cost[i-1] > cost[i]:
            cost[i] = cost[i]+cost[i-1]
        if cost[i]>max_v:
            max_v = cost[i]
    print(max_v)