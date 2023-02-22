from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

N, M, K = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]
visited = [[[float('inf')]*(K+1) for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0, K))
visited[0][0][K] = 1
while q:
    r, c, k = q.popleft()
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < N and 0 <= nc < M:
            if maps[nr][nc] == '0':
                if visited[nr][nc][k] > visited[r][c][k] + 1:
                    visited[nr][nc][k] = visited[r][c][k] + 1
                    q.append((nr, nc, k))
            else:
                if k > 0 and visited[nr][nc][k-1] > visited[r][c][k] + 1:
                    visited[nr][nc][k-1] = visited[r][c][k] + 1
                    q.append((nr, nc, k-1))

print(min(visited[N-1][M-1]) if min(visited[N-1][M-1]) != float('inf') else -1)