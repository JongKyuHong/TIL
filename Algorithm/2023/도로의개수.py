import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
lst = [list(map(int, input().split())) for _ in range(K)]
visited = [[0]*(M+1) for _ in range(N+1)]
visited[0][0] = 1
for i in range(1, N+1):
    if [i-1, 0, i, 0] in lst or [i, 0, i-1, 0] in lst:
        break
    visited[i][0] = 1
for i in range(1, M+1):
    if [0, i-1, 0, i] in lst or [0, i, 0, i-1] in lst:
        break
    visited[0][i] = 1
for i in range(1, N+1):
    for j in range(1, M+1):
        visited[i][j] = visited[i-1][j] + visited[i][j-1]
        if [i-1, j, i, j] in lst or [i, j, i-1, j] in lst:
            visited[i][j] -= visited[i-1][j]
        if [i, j-1, i, j] in lst or [i, j, i, j-1] in lst: 
            visited[i][j] -= visited[i][j-1]

print(visited[N][M])
