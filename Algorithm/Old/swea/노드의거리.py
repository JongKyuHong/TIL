from collections import deque

def bfs(start):
    visited[start] = 1
    que = deque([start])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                distance[i] = distance[v] + 1
                visited[i] = 1


for test_case in range(int(input())):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int,input().split())
    visited = [0]*(v+1)
    distance = [0]*(v+1)
    bfs(s)
    print(f'#{test_case+1} {distance[g]}')