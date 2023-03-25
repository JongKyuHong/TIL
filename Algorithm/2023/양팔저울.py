from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global min_v
    q = deque()
    q.append((1, 0))
    while q:
        val, cnt = q.popleft()
        if visited[val] < cnt:
            continue
        visited[val] = cnt
        for i in range(1,7):
            if val + i == 100:
                min_v = min(min_v, cnt)
                continue
            elif val + i < 100:
                if val+i in ladder:
                    q.append((ladder[val+i], cnt+1))
                else:
                    q.append((val+i, cnt+1))
                

N, M = map(int, input().split())
INF = float('inf')
min_v = INF
visited = [INF]*(101)
ladder = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    ladder[u] = v
visited[1] = 0
bfs()
print(min_v+1)


