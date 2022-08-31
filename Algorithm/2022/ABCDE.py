import sys
import heapq
input = sys.stdin.readline

def dfs(idx, depth):
    global ans
    visited[idx] = 1
    if depth == 4:
        ans = 1
        return
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth+1)
            visited[i] = 0

n, m = map(int, input().split()) # 사람수, 관계수
graph = [[] for _ in range(n)]
visited = [0] * 2001
ans = 0
for _ in range(m):
    a, b = map(int, input().split()) # a와 b가 친구다
    graph[a].append(b)
    graph[b].append(a)

res = 0
for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if ans:
        break
if ans:
    print(1)
else:
    print(0)
