import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
res = []
def dfs(start, next, sum_v, idx):
    global ans
    if idx == N-1:
        if graph[next][start] != 0:
            ans = min(ans, sum_v+graph[next][start])
        return

    for i in range(N):
        if graph[next][i] != 0 and i != start and i not in res:
            res.append(i)
            dfs(start, i, sum_v + graph[next][i], idx+1)
            res.pop()

for i in range(N):
    dfs(i, i, 0, 0)

print(ans)