# 돌다리   
from collections import deque         
def bfs(n, m):
    global res
    q = deque()
    q.append((n,1))
    visited[n] = 1
    while q:
        n,cnt = q.popleft()
        if cnt > res:
            continue
        for i in range(6):
            if i == 0:
                nr = n + 1
            elif i == 1:
                nr = n - 1
            elif i == 2:
                nr = n + a
            elif i == 3:
                nr = n + b
            elif i == 4:
                nr = n * a
            elif i == 5:
                nr = n * b
            elif i == 6:
                nr = -1*(n*a)
            else:
                nr = -1*(n*b)
            if 0 <= nr <= 100000 and not visited[nr]:
                visited[nr] = 1
                if nr == m:
                    res = min(res, cnt)
                    break
                q.append((nr,cnt+1))
a,b,n,m = map(int, input().split())
visited = [0]*100001
res = 100000
if n != m:
    bfs(n,m)
    print(res)
else:
    print(0)
