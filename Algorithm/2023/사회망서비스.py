import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(N+1)
dp = [[0]*2 for _ in range(N+1)]

def find(node):
    if len(tree[node]) == 0:
        dp[node][0] = 0
        dp[node][1] = 1
    else:
        for i in tree[node]:
            if not visited[i]:
                visited[i] = 1
                find(i)
                dp[node][1] += min(dp[i][0], dp[i][1])
                dp[node][0] += dp[i][1]
        dp[node][1] += 1
visited[1] = 1
find(1)
print(min(dp[1][0],dp[1][1]))
