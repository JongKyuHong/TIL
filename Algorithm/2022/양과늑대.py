from collections import deque

max_sheep = -1
def dfs(start, sheep, wolf, graph, visited, info):
    if sheep <= wolf:
        global max_sheep
        max_sheep = max(max_sheep, sheep)
        return
    for g in graph[start]:
        if not visited[g]:
            visited[g] = 1
            if info[g] == 0:
                dfs(g, sheep+1, wolf, graph, visited, info)
            else:
                dfs(g, sheep, wolf+1, graph, visited, info)
            visited[g] = 0

def solution(info, edges):
    global max_sheep
    graph = [[] for _ in range(len(info))]
    #max_sheep = -1
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    visited = [0]*len(info)
    visited[0] = 1
    sheep, wolf = 1, 0
    dfs(0, sheep, wolf, graph, visited, info)
    return max_sheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))