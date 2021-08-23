t = int(input())


def dfs(v, e, graph, s, g):
    visited = [False for _ in range(v+1)]
    to_visits = [s]
    while to_visits:
        current = to_visits.pop()
        if not visited[current]: # 방문하지 않았다면
            visited[current] = True
            to_visits += graph[current]

    return visited[g]

for tc in range(1,t+1):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int,input().split())
        graph[start].append(end)
    
    s, g = map(int,input().split())

    print(dfs(v,e,graph,s,g))


