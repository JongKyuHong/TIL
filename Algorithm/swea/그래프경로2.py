def bfs(graph, start, visited):
    visited[start] = 1
    que = [start]
    while que:
        v = que.pop(0)
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = 1

for test_case in range(int(input())):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
    print(graph)
    visited = [0] * (v+1)
    s, g = map(int,input().split())
    bfs(graph,s,visited)
    print(f'#{test_case+1} {visited[g]}')



