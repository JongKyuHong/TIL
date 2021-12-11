def dfs(nodes,visited,index):
    visited[index] = 1
    for node in nodes[index]:
        if visited[node] == 0:
            dfs(nodes,visited,node)


for _ in range(10):
    tc, way = map(int,input().split())
    array = list(map(int,input().split()))
    nodes = [[] for _ in range(100)]
    visited = [0]*100
    for i in range(0,len(array),2):
        start = array[i]
        end = array[i+1]
        nodes[start].append(end)
    s, g =0, 99
    dfs(nodes,visited,s)
    if visited[g] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')