from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))
horse = ((-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2))
INF = float('inf')
k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]


def bfs(r, c, k):
    q = deque()
    q.append((r, c, k))
    visited = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
    while q:
        r, c, k = q.popleft()
        if r == h-1 and c == w-1: return visited[r][c][k]
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 0 and visited[nr][nc][k] == 0:
                visited[nr][nc][k] = visited[r][c][k] + 1
                q.append((nr,nc,k))

        if k > 0:
            for dr, dc in horse:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 0 and visited[nr][nc][k-1] == 0:
                    visited[nr][nc][k-1] = visited[r][c][k] + 1
                    q.append((nr,nc,k-1))
    return -1


print(bfs(0, 0, k))