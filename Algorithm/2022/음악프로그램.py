from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    data = list(map(int, input().split()))
    a, data2 = data[0], data[1:]
    for i in range(a-1):
        graph[data2[i]].append(data2[i+1])
        indegree[data2[i+1]] += 1

def find():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)
find()