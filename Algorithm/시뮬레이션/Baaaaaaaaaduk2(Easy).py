from collections import deque
from itertools import combinations
import copy
import sys 
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))


def bfs(r, c):
    global visited
    q = deque()
    q.append((r, c))
    flag = 0
    cnt = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]: 
                if lst2[nr][nc] == 2:
                    cnt += 1
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                elif lst2[nr][nc] == 0:
                    flag = 1

    return cnt if not flag else 0

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

coordinate = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            coordinate.append((i, j))

# 돌을 어디에다가 둘것인가
# 2개이기 때문에 모든경우의 수를 다고려??

# 돌이 죽었는지 판단하는 로직
# bfs를 이용

answer = 0
for com in combinations(coordinate, 2):
    lst2 = copy.deepcopy(lst)
    for a, b in com:
        lst2[a][b] = 1

    visited = [[0]*M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2 and not visited[i][j]:
                visited[i][j] = 1
                ans += bfs(i, j)
    answer = max(answer, ans)
print(answer)



                    