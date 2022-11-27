from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
while 1:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    
    graph = [input().rstrip() for _ in range(r)]
    new_graph = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                new_graph[i][j] = -1
            else:
                q = deque()
                q.append((i, j))
                while q:
                    i, j = q.popleft()
                    for dr, dc in delta:
                        nr, nc = dr+i, dc+j
                        if 0 <= nr < r and 0 <= nc < c:
                            if graph[nr][nc] == '*':
                                new_graph[i][j] += 1
    
    for i in new_graph:
        for j in i:
            if j == -1:
                print('*',end='')
            else:
                print(j,end='')
        print()

