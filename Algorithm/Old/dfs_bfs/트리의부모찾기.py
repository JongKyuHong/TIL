n = int(input())
graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(1,n):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
    
def dfs(cur):
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
            parent[next] = cur
            dfs(next)
dfs(1)
    
for i in range(2, n+1):
    print(parent[i])
    

