import sys
input = sys.stdin.readline

def rotate(n, arr):
    lst = [[0]*n for _ in range(n)]
    for i in range(n):
        lst[i][n//2] = arr[i][i]
    for i in range(n):
        lst[i][n-i-1] = arr[i][n//2]
    for i in range(n):
        lst[n//2][n-i-1] = arr[i][n-i-1]
    for i in range(n):
        lst[n-i-1][n-i-1] = arr[n//2][n-i-1]
    return lst

for _ in range(int(input())):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    if d < 0:
        d = -d
        d = 360-d
    if d == 360:
        for i in graph:
            print(*i)
    else:
        while d > 0:
            d -= 45
            lst = rotate(n, graph)
            for i in range(n):
                for j in range(n):
                    if lst[i][j] == 0:
                        lst[i][j] = graph[i][j]
            graph = lst[:]
        for i in graph:
            print(*i)
