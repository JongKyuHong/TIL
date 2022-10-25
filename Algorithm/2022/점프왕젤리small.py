from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
delta = ((0,1),(1,0))
q = deque()
q.append((0, 0, graph[0][0]))
visited = [[0]*n for _ in range(n)]
visited[0][0] = 1
while q:
    r, c, value = q.popleft()
    if r == n-1 and c == n-1:
        print("HaruHaru")
        exit()

    for dr, dc in delta:
        nr, nc = (value*dr)+r, (value*dc)+c
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            visited[nr][nc] = 1
            q.append((nr, nc, graph[nr][nc]))
    
print("Hing")