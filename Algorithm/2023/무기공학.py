import sys
input = sys.stdin.readline

def find(i, j, value):
    if j == M:
        i += 1
        j = 0
    if i == N:
        global max_v
        max_v = max(max_v, value)
        return
    if not visited[i][j]:
        if i+1 < N and j+1 < M:
            if not visited[i+1][j] and not visited[i][j+1]:
                visited[i][j] = 1
                visited[i+1][j] = 1
                visited[i][j+1] = 1
                find(i, j+1, value + (lst[i][j]*2 + lst[i+1][j] + lst[i][j+1]))
                visited[i][j] = 0
                visited[i+1][j] = 0
                visited[i][j+1] = 0
        if j-1 >= 0 and i-1 >= 0:
            if not visited[i][j-1] and not visited[i-1][j]:
                visited[i][j] = 1
                visited[i-1][j] = 1
                visited[i][j-1] = 1
                find(i, j+1, value + (lst[i][j]*2 + lst[i-1][j] + lst[i][j-1]))
                visited[i][j] = 0
                visited[i-1][j] = 0
                visited[i][j-1] = 0
        if i-1 >= 0 and j + 1 < M:
            if not visited[i-1][j] and not visited[i][j+1]:
                visited[i][j] = 1
                visited[i-1][j] = 1
                visited[i][j+1] = 1
                find(i, j+1, value + (lst[i][j]*2 + lst[i-1][j] + lst[i][j+1]))
                visited[i][j] = 0
                visited[i-1][j] = 0
                visited[i][j+1] = 0
        if j-1 >= 0 and i+1 < N:
            if not visited[i][j-1] and not visited[i+1][j]:
                visited[i][j] = 1
                visited[i][j-1] = 1
                visited[i+1][j] = 1
                find(i, j+1, value + (lst[i][j]*2 + lst[i][j-1] + lst[i+1][j]))
                visited[i][j] = 0
                visited[i][j-1] = 0
                visited[i+1][j] = 0
    find(i, j+1, value)
            
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
if N < 2 or M < 2:
    print(0)
else:
    visited = [[0]*M for _ in range(N)]
    max_v = 0
    find(0, 0, 0)
    print(max_v)

# 4칸에서 가장 
