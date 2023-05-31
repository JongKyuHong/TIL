from collections import deque
import sys 
input = sys.stdin.readline

N, K = map(int, input().split())

lst = list(map(int, input().split()))
q = deque()
visited = set()
for i in lst:
    q.append([i, 0])
    visited.add(i)
# 앞 뒤 확인
ans = 0
idx = 1
while K > 0:
    val, dist = q.popleft()
    if val+1 not in visited:
        ans += dist+1
        q.append([val+1, dist+1])
        visited.add(val+1)
        K -= 1
    if K == 0:
        break
    if val-1 not in visited:
        ans += dist+1
        q.append([val-1, dist+1])
        visited.add(val-1)
        K -= 1
print(ans)

# visited를 set으로하면 시간오류가 안난다.