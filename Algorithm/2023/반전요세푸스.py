from collections import deque
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
q = deque(range(1, N+1))
idx = 0
cnt = 0
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft())
    cnt += 1
    if cnt == M:
        q.reverse()
        cnt = 0