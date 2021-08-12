import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
min1 = min(map(min,li))
max1 = max(map(max,li))
leasttime = 1e9

for i in range(min1,max1+1):
    pluscnt = 0  # 쌓아야 하는 블록수
    minuscnt = 0  # 치울애들
    for j in range(n):
        for k in range(m):
            h = li[j][k] - i
            if h>0:
                minuscnt += h
            elif h<0:
                pluscnt -= h
    if minuscnt+b >= pluscnt:
        time = minuscnt*2+pluscnt
        if leasttime >= time:
            leasttime = time
            resultHeight = i
print(leasttime, resultHeight)