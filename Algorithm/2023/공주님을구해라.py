from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

N, M, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[[float('inf')]*M for _ in range(N)] for _ in range(2)]
q =  deque()
q.append((0,0,0))
visited[0][0][0] = 0
while q:
    r, c, sword = q.popleft()
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < N and 0 <= nc < M:
            if visited[sword][nr][nc] > visited[sword][r][c] + 1:
                if sword == 1:
                    visited[sword][nr][nc] = visited[sword][r][c] + 1
                    q.append((nr, nc, sword))
                else:
                    if lst[nr][nc] != 1:
                        if lst[nr][nc] == 2:
                            visited[1][nr][nc] = visited[sword][r][c] + 1
                            q.append((nr, nc, 1))
                        else:
                            visited[sword][nr][nc] = visited[sword][r][c] + 1
                            q.append((nr, nc, 0))

ans = min(visited[0][N-1][M-1], visited[1][N-1][M-1])
if ans <= T:
    print(ans)
else:
    print("Fail")