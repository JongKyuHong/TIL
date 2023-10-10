import heapq
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for i in range(N + 1)]
indegree = [0]*(N+1)
q = []
for i in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    lst[a].append(b) # b보다 a가 먼저 있어야함    

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    now = heapq.heappop(q)
    result.append(now)
    for i in lst[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

for i in result:
    print(i, end=' ')

