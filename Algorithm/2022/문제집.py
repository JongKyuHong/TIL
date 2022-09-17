from collections import deque
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

def find():
    #q = deque()
    q = []
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        #now = q.popleft()
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                #q.append(i)
                heapq.heappush(q, i)
    for i in result:
        print(i, end=' ')

find()