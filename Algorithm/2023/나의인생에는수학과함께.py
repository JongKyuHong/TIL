from collections import deque
import sys
input = sys.stdin.readline

#delta = ((0,1),(0,-1),(1,0),(-1,0))
delta = ((0,1),(1,0))
def bfs():
    q = deque()
    q.append((0, 0, int(graph[0][0]), ''))
    while q:
        r, c, val, op = q.popleft()
        if r == N-1 and c == N-1:
            global max_v, min_v
            max_v = max(max_v, val)
            min_v = min(min_v, val)
            continue
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N:
                if op:
                    graph[nr][nc] = int(graph[nr][nc])
                    if op == '+':
                        val2 = val + graph[nr][nc]
                    elif op == '-':
                        val2 = val - graph[nr][nc]
                    elif op == '*':
                        val2 = val * graph[nr][nc]
                    q.append((nr, nc, val2, ''))
                else:
                    q.append((nr, nc, val, graph[nr][nc]))

N = int(input())
graph = [list(input().rstrip().split()) for _ in range(N)]
max_v, min_v = -float('inf'), float('inf')
bfs()
print(max_v, min_v)