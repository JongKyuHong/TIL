import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def find(node):
    if len(graph[node]) == 0:
        dp[node][0] = 0
        dp[node][1] = 1
    else:
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                find(i)
                dp[node][0] += dp[i][1]
                dp[node][1] += min(dp[i][0], dp[i][1])
        dp[node][1] += 1
visited = [0]*(N+1)
dp = [[0]*2 for _ in range(N+1)]
visited[1] = 1
find(1)
print(min(dp[1][0],dp[1][1]))