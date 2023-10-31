import sys 
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
lst = [[0]*101 for _ in range(101)]

N = int(input())
coordinate = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    current = [d]
    for i in range(g):
        tmp = []
        for j in range(len(current)-1, -1, -1):
            tmp.append((current[j]+1) % 4)
        current += tmp
    lst[x][y] = 1
    for i in range(len(current)):
        x = x + dx[current[i]]
        y = y + dy[current[i]]
        lst[x][y] = 1
result = 0
for i in range(100):
    for j in range(100):
        if (lst[i][j] and lst[i][j+1] and lst[i+1][j] and lst[i+1][j+1]):
            result += 1
print(result)