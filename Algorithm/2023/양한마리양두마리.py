from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and lst[nr][nc] == '#':
                q.append((nr, nc))
                visited[nr][nc] = 1

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    lst = [list(input().rstrip()) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if lst[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
