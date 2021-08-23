t = int(input())


def go(v):
    #path.append(v)
    visited[v] = True
    for new_v in graph[v]:
        if not visited[new_v]:
            go(new_v)



for tc in range(1,t+1):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int,input().split())
        graph[start].append(end)
    
    s, g = map(int,input().split())
    visited = [False for _ in range(v+1)]
    #path = []

    print(go(s))
    #print(path)

