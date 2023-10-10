from collections import deque
import sys 
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
cnt = 1 
visited = [[0]*N for _ in range(N)]
cnt2 = 1
def bfs(i, j, type):
    global cnt, cnt2
    q = deque()
    q.append((i, j))
    if type == 0:
        visited[i][j] = cnt
    else:
        visited2[i][j] == cnt2
    while q:
        r, c = q.popleft()  
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N:
                if type == 0:
                    if not visited[nr][nc] and lst[nr][nc] == lst[i][j]:
                        visited[nr][nc] = cnt
                        q.append((nr, nc))
                else:
                    if not visited2[nr][nc]:
                        if lst[i][j] == lst[nr][nc]:
                            visited2[nr][nc] = cnt2
                            q.append((nr, nc))
                        elif lst[i][j] == 'R':
                            if lst[nr][nc] == 'R' or lst[nr][nc] == 'G':    
                                visited2[nr][nc] = cnt2
                                q.append((nr, nc))
                        elif lst[i][j] == 'G':
                            if lst[nr][nc] == 'R' or lst[nr][nc] == 'G':
                                visited2[nr][nc] = cnt2
                                q.append((nr, nc))

            
visited2 = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 0)
            cnt += 1

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs(i, j, 1)
            cnt2 += 1
print(cnt-1, cnt2-1)




