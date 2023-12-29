from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))


def find(r, c):
    global total_M
    q = deque()
    q.append((r, c))
    visited = [[0]*N for _ in range(N)]
    if lst[r][c] == 2:
        lst[r][c] = 0
        total_M -= 1
        return [r, c, 0]
    rv, cv = -1, -1
    value = float('inf')
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if lst[nr][nc] == 2:
                    if visited[nr][nc] < value:
                        value = visited[nr][nc]
                        rv, cv = nr, nc
                    elif visited[nr][nc] == value: 
                        if nr < rv:
                            rv, cv = nr, nc
                        elif nr == rv:
                            if nc < cv:
                                rv, cv = nr, nc
                q.append((nr, nc))

    if rv != -1 and cv != -1:
        lst[rv][cv] = 0
        total_M -= 1
    return [rv, cv, value]

def check_dist(r, c, er, ec):
    q = deque()
    q.append((r, c))
    visited = [[0]*N for _ in range(N)]
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if nr == er and nc == ec:
                    return visited[nr][nc]
                q.append((nr, nc))
    return -1
N, M, K = map(int, input().split())
total_M = M
lst = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
R -= 1; C -= 1

coordinate = {}
for _ in range(M):
    start_r, start_c, end_r, end_c = map(int, input().split())
    start_r -= 1;start_c -=1;end_r -= 1;end_c -= 1    
    lst[start_r][start_c] = 2
    dist = check_dist(start_r, start_c, end_r, end_c)
    if dist == -1:
        print(-1)
        exit()
    coordinate[start_r, start_c] = [end_r, end_c, dist]


while 1:
    start_r, start_c, value = find(R, C)
    if start_r == -1 and start_c == -1:
        print(-1)
        break
    if value > K:
        print(-1)
        break
    K -= value
    end_r, end_c, dist = coordinate[start_r, start_c]
    if dist > K:
        print(-1)
        break
    del coordinate[start_r, start_c]
    K -= dist
    K += dist*2
    if total_M == 0:
        print(K)
        break
    R, C = end_r, end_c