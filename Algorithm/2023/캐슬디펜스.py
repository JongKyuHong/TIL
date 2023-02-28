from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt_enemy = 0 # 처음 적의 수 
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt_enemy += 1
dx = [0,-1,0]
dy = [-1,0,1]

def calc(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

def find_enemy(col):
    q = deque()
    q.append((N-1, col))
    while q:
        r, c = q.popleft()
        if calc(N, r, col, c) > D:
            return False
        if board[r][c] == 1:
            return (r, c)
        for i in range(3):
            nr, nc = r+dx[i], c+dy[i]
            if 0 <= nr < N and 0 <= nc < M:
                q.append((nr, nc))

def move_enemy():
    for j in range(M):
        for i in range(N-2, -1, -1):
            board[i+1][j] = board[i][j]
    for i in range(M):
        board[0][i] = 0

def del_enemy():
    cnt = 0
    for i in range(M):
        if board[N-1][i] == 1:
            cnt += 1
    return cnt

for combi in combinations(list(range(M)), 3):
    del_cnt = 0
    curr_enemy = cnt_enemy
    board = copy.deepcopy(graph)
    while curr_enemy > 0:
        tmp = set()
        for c in combi:
            enemy_pos = find_enemy(c)
            if enemy_pos:
                tmp.add(enemy_pos)
        for x, y in tmp:
            board[x][y] = 0
        
        del_cnt += len(tmp)
        curr_enemy -= len(tmp)
        curr_enemy -= del_enemy()
        move_enemy()
    answer = max(answer, del_cnt)
print(answer)
