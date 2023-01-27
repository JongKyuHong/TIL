from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
edges = defaultdict(list)
visited = [0 for _ in range(N+1)]
cost = [0] + [int(x) for x in input().split()]
dp = [[0, cost[i]]*2 for i in range(N+1)] # dp[i][0] i마을을 선정x, dp[i][1] i 마을을 선정

def dfs(cur):
    visited[cur] = 1
    for u in edges[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0], dp[u][1])


for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
dfs(1)
print(dp)
print(edges)
print(max(dp[1][1], dp[1][0]))
