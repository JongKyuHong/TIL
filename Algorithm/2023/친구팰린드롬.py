import sys
input = sys.stdin.readline

def dfs(vn, cnt):
    if vn == N:
        return cnt
    if visited[vn]:
        return dfs(vn+1, cnt)
    res = 0
    for i in graph[vn]:
        if not visited[i]:
            visited[i] = 1
            res = max(res, dfs(vn+1, cnt+1))
            visited[i] = 0
    return max(res, dfs(vn+1, cnt))

N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0]*21
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        graph[v].append(u)  
    else:
        graph[u].append(v)  

res = dfs(0, 0)
res *= 2
if N > res:
    res += 1
print(res)
