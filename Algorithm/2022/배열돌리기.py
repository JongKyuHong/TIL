import copy

def rotate(graph, graph2):
    global standard
    for i in range(n):
        graph2[i][standard] = graph[i][i]
        graph2[i][n-i-1] = graph[i][standard]
        graph2[standard][n-i-1] = graph[i][n-i-1]
        graph2[i][i] = graph[standard][i]
    return graph2


for _ in range(int(input())):
    n, d = map(int, input().split())
    if n == 1:
        print(int(input()))
    else:
        graph = [list(map(int, input().split())) for _ in range(n)]
        graph2 = copy.deepcopy(graph)
        array = []
        standard = n // 2
        if d < 0:
            cnt = abs(d) // 45
            cnt = cnt % 8
            cnt = 8-cnt
            for i in range(cnt):
                array = rotate(graph, graph2)
                graph = array
                graph2 = copy.deepcopy(graph)
        elif d > 0:
            cnt = d // 45
            cnt = cnt % 8
            for i in range(cnt):
                array = rotate(graph, graph2)
                graph = array
                graph2 = copy.deepcopy(graph)
        for i in graph:
            print(*i)