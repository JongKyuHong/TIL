import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) # 회사의 직원수, 최초의 칭찬의 횟수
parent = list(map(int, input().split()))
dp = [0]*(n+1)
for _ in range(m):
    i, w = map(int, input().split())
    dp[i] += w

def dfs(idx):
    if idx == 1:
        dfs(idx+1)
        return
    else:
        if idx == n+1:
            return
        p = parent[idx-1]
        #print(p, idx,'dd')
        dp[idx] += dp[p]
        dfs(idx+1)
dfs(1)
print(*dp[1:])
