from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
dp = [0] * (n+1)
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time = data[0]
    dp[i] = time
    if len(data) > 2:
        cnt = data[1]
        data2 = data[2:]
        for j in range(cnt):
            graph[data2[j]].append((i, time))
            indegree[i] += 1

def find():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now= q.popleft()
        for next_node, next_time in graph[now]:
            indegree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[now] + next_time)
            if indegree[next_node] == 0:
                q.append((next_node))

find()
print(max(dp))