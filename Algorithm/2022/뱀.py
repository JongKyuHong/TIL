from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 보드의 크기
graph = [[0]*N for _ in range(N)]
K = int(input()) # 사과의 갯수

apples = []
for i in range(K):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2
L = int(input()) # 뱀의 방향변환횟수
delta = []
for _ in range(L):
    time, dir = input().split()
    delta.append([time, dir])


q = deque()
body = deque()
body.append((0, 0))
q.append((0, 0, 0))
dir = ((0,1),(-1,0),(0,-1),(1,0))
idx = 0
delta_idx = 0
ans = 0
while q:
    time, r, c = q.popleft()
    time += 1
    nr = r+dir[idx][0]
    nc = c+dir[idx][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in body:
        ans = time
        break
    else:
        if graph[nr][nc] == 0:
            body.popleft()
            body.append((nr, nc))
            q.append((time, nr, nc))
        elif graph[nr][nc] == 2:
            body.append((nr, nc))
            q.append((time, nr, nc))
    if delta_idx < L:
        if time == int(delta[delta_idx][0]):
            value = delta[delta_idx][1]
            delta_idx += 1
            if value == 'L':
                idx += 1
                if idx == 4:
                    idx = 0
            else:
                idx -= 1
                if idx == -1:
                    idx = 3
print(ans)