import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
n = int(input())
m = int(input())

path = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    path[start].append((end,cost))


start, end = map(int, input().split())
distance = [INF] * (n+1)
distance[start] = 0

q = deque([(start, 0)])
while q:
    now, credit = q.popleft()
    if distance[now] < credit:
        continue
    for destination, cost in path[now]:
        cost = credit + cost
        if distance[destination] > cost:
            distance[destination] = cost
            q.append((destination,cost))
print(distance[end])