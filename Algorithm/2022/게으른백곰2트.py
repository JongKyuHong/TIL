import sys
input = sys.stdin.readline

n, k = map(int , input().split()) # n개의 얼음양동이, 좌우 k만큼 닿음
lst = [0] *4000001
max_x = 0
min_x = float('inf')
for _ in range(n):
    g, x = map(int, input().split())
    max_x = max(max_x, x)
    min_x = min(min_x, x)
    lst[x] = g

if max_x - min_x <= k*2:
    print(sum(lst[min_x:max_x+1]))
else:
    idx = 0
    res = 0
    target = sum(lst[idx:idx+(2*k)])
    while idx+k <= max_x:
        target += lst[idx+(2*k)]
        res = max(res, target)
        target -= lst[idx]
        idx += 1
    print(res)