from collections import deque
import sys 
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))
count = 1

def bfs(r, c):
    global count
    q = deque()
    q.append((r, c))
    visited[r][c] = count
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == '1' and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = count

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][j] == '1' and not visited[i][j]:
            bfs(i, j)
            count += 1

count_home = [0]*(count)

for i in range(N):
    for j in range(N):
        count_home[visited[i][j]] += 1

count_home = count_home[1:]
count_home.sort()
print(count-1)
for i in count_home:
    print(i)

