from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

dp = [0] * (n+1)
def find():
    q = deque()
    #result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = 1
    while q:
        now = q.popleft()
        #result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                dp[i] = dp[now] + 1
                q.append(i)
    
    # for i in result:
    #     print(i, end=' ')
find()
print(*dp[1:])
