import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))

res = []
visited = [0] * (N+1)
def find(v, k):
    if k == M:
        ans = []
        for i in v:
            ans.append(i)
        res.append(ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans = [S[i]]
            find(v+ans, k+1)
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    find([S[i]], 1)
    visited[i] = 0

res.sort()
for i in res:
    print(*i)