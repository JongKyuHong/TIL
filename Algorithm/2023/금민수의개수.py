from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
q = deque()
q.append(4)
q.append(7)
ans = 0
while q:
    f = q.popleft()
    if f <= B:
        if A <= f:
            ans += 1
        q.append(f*10+4)
        q.append(f*10+7)
print(ans)