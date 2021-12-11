from collections import deque

def bfs(x):
    global k
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in range(3):
            if i == 0:
                dx = x + 1
            elif i == 1:
                dx = x - 1
            else:
                dx = x * 2
            if dx > k+1 or dx < 0:
                continue
            if visited[dx] > visited[x] + 1:
                visited[dx] = visited[x] + 1
                q.append(dx)
  

n, k = map(int, input().split())
if n > k:
    print(n-k)
    exit()
INF = float('inf')
visited = [INF] * (10**6+2)
visited[n] = 0
bfs(n)
print(visited[k])