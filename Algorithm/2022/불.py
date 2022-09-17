from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r1, c1, r2, c2):
    q = deque()
    q.append((r1, c1, 0, 0)) # r,c,거리,불인지 지훈인지 불 0 지훈 1
    visited[0][r1][c1] = 1
    q.append((r2, c2, 0, 1))
    visited[1][r2][c2] = 1
    while q:
        r, c, dist, j_type = q.popleft()
        if j_type == 0:
            for dr, dc in delta:
                nr, nc = dr+r, dc+c
                if 0 <= nr < a and 0 <= nc < b and not visited[0][nr][nc] and graph[nr][nc] != '#':
                    dist += 1
                    visited[0][nr][nc] = 1
                    q.append((nr, nc, dist, 0))
        else:
            for dr, dc in delta:
                nr, nc = dr+r, dc+c
                if 0 <= nr < a and 0 <= nc < b and not visited[0][nr][nc] and not visited[1][nr][nc] and graph[nr][nc] != '#':
                    dist += 1
                    if nr == 0 or nr == a-1 or nc == 0 or nc == b-1:
                        return dist+1
                    visited[1][nr][nc] = 1
                    q.append((nr, nc, dist, 1))
    return 'IMPOSSIBLE'

a, b = map(int, input().split())
jihun = []
fire = []
graph = []
for i in range(a):
    data = list(input())
    for j in range(b):
        if data[j] == 'J':
            jihun.append((i, j))
        elif data[j] == 'F':
            fire.append((i, j))
    graph.append(data)
if jihun[0][0] == 0 or jihun[0][0] == a-1 or jihun[0][1] == 0 or jihun[0][1] == b-1:
    print(1)
    exit()
visited = [[[0 for _ in range(b)] for _ in range(a)] for _ in range(2)] # 0일때 불, 1일때 지훈
print(bfs(fire[0][0],fire[0][1],jihun[0][0],jihun[0][1]))
# #벽, .지나가는공간, J지훈이 초기위치, F불이난 공간
