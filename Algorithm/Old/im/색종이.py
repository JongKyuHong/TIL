n = int(input())
graph = [[0]*1001 for _ in range(1001)]
for mark in range(1,n+1):
    a1, a2, width, height = map(int, input().split())
    x, y = a1, 1000-a2
    for i in range(y-height,y):
        for j in range(x,x+width):
            graph[i][j] = mark

res = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        res[graph[i][j]] += 1
for i in range(1,n+1):
    print(res[i])


