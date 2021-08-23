def dfs(node_index,visited,nodes):
    visited[node_index] = 1
    for node in nodes[node_index]:
        if visited[node] != 1:
            dfs(node,visited,nodes)
        

for test_case in range(1):
    tc, length = map(int,input().split())
    array = list(map(int,input().split()))
    nodes = [[] for _ in range(100)]
    visited = [0] * 100
    for i in range(0,len(array),2):
        start = array[i]
        end = array[i+1]
        nodes[start].append(end)
    s,g = 0,99
    dfs(s,visited,nodes)
    answer = 0
    if visited[g] == 1:
        answer = 1
    print(f'#{test_case} {answer}')

