t = int(input())

def dfs(nodes,visited,index):
    visited[index] = 1  # 방문표시
    for node in nodes[index]:
        if visited[node] == 0:
            dfs(nodes,visited,node)

for test_case in range(1,t+1):
    v,e = map(int,input().split())
    nodes = [[] for _ in range(v+1)]  # 0~v까지
    for _ in range(e):
        start,end = map(int,input().split())
        nodes[start].append(end)
    print(nodes)
    s,g = map(int,input().split())  # 출발노드s , 도착노드g
    visited = [0] * (v+1)
    dfs(nodes,visited,s)

    if visited[g] == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
