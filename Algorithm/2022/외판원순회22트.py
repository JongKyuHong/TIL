import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')
def dfs(node, cost, cnt):
    if cnt == n:
        global res
        if not visited[0] and graph[node][0]:
            res = min(res,cost + graph[node][0])
        return
    for i in range(n):
        if not visited[i] and graph[node][i]: 
            visited[i] = 1
            dfs(i, cost+graph[node][i], cnt+1)
            visited[i] = 0

visited = [0] * n
dfs(0, 0, 1)
print(res)