import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
visited = [0] * (N+1)
res = []
def find(v, k, idx):
    if k == M:
        ans = []
        for i in v:
            ans.append(i)
        res.append(ans)
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            ans = [S[i]]
            find(v+ans, k+1, i)
            visited[i] = 0


for i in range(N):
    find([S[i]], 1, i)

res.sort()
for i in res:
    print(*i)