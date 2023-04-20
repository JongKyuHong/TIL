from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')

M, N = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(M)]
r, c, d = map(int, input().split())
end_r, end_c, end_d = map(int, input().split())

q = deque()
q.append((r-1, c-1, d))
visited = [[[INF]*N for _ in range(M)] for _ in range(5)]
visited[d][r-1][c-1] = 0

while q:
    r, c, d = q.popleft()
    cnt = 0
    nr, nc = r, c
    while cnt < 3:
        if d == 1:
            nr, nc = nr, nc+1
        elif d == 2:
            nr, nc = nr, nc-1
        elif d == 3:
            nr, nc = nr+1, nc
        else:
            nr, nc = nr-1, nc
        if 0 <= nr < M and 0 <= nc < N and not factory[nr][nc]:
            if visited[d][nr][nc] > visited[d][r][c] + 1:
                visited[d][nr][nc] = visited[d][r][c] + 1
                q.append((nr, nc, d))
        else:
            break
        cnt += 1
    if d == 1 or d == 2:
        if visited[4][r][c] == INF or visited[4][r][c] > visited[d][r][c] + 1:
            visited[4][r][c] = visited[d][r][c] + 1
            q.append((r, c, 4))
        if visited[3][r][c] == INF or visited[3][r][c] > visited[d][r][c] + 1:
            visited[3][r][c] = visited[d][r][c] + 1
            q.append((r, c, 3))
    else:
        if visited[1][r][c] == INF or visited[1][r][c] > visited[d][r][c] + 1:
            visited[1][r][c] = visited[d][r][c] + 1
            q.append((r, c, 1))
        if visited[2][r][c] == INF or visited[2][r][c] > visited[d][r][c] + 1:
            visited[2][r][c] = visited[d][r][c] + 1
            q.append((r, c, 2))
print(visited[end_d][end_r-1][end_c-1])

