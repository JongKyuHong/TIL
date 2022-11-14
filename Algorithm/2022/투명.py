import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*101 for _ in range(101)]
for _ in range(n):
    r1,c1,r2,c2 = map(int, input().split())
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            graph[i][j] += 1

res = 0
for i in range(1,101):
    for j in range(1,101):
        if graph[i][j] > m:
            res += 1
print(res)