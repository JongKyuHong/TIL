from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 걷거나 순간이동 x-1 , x+1로 이동 2*x
res = []
ans = sys.maxsize
q = deque()
q.append((n, 0))
visited = [0] * 100001
while q:
    now, time = q.popleft()
    visited[now] = 1
    if now == k:
        if ans > time:
            ans = time
            res = []
            res.append(time)
        elif ans == time:
            res.append(time)

    now2 = now-1
    if 0 <= now2 < 100001 and not visited[now2]:
        q.append((now2, time+1))
    
    now2 = now+1
    if 0 <= now2 < 100001 and not visited[now2]:
        q.append((now2, time+1))

    now2 = now*2
    if 0 <= now2 < 100001 and not visited[now2]:
        q.append((now2, time+1))

print(ans)
print(len(res))