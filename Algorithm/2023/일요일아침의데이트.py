import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
S, F = [], []
garbage = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'F':
            F = [i, j]
        elif graph[i][j] == 'S':
            S = [i, j]
        elif graph[i][j] == 'g':
            garbage.append([i, j])

for x, y in garbage:
    for dr, dc in delta:
        nr, nc = dr+x, dc+y
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == '.':
            graph[nr][nc] = '#'

q = []
heapq.heappush(q, (0, 0, S[0], S[1]))
visited = [[0]*M for _ in range(N)]
visited[S[0]][S[1]] = 1
while q:
    g1, g2, r, c = heapq.heappop(q)
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            if graph[nr][nc] == '.':
                heapq.heappush(q, (g1, g2, nr, nc))
            elif graph[nr][nc] == '#':
                heapq.heappush(q, (g1, g2+1, nr, nc))
            elif graph[nr][nc] == 'g':
                heapq.heappush(q, (g1+1, g2, nr, nc))
            elif graph[nr][nc] == 'F':
                print(g1, g2)
                break   
