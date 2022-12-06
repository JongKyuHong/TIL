import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def find_2nd(graph, r, c):
    res = []
    for i in range(r, r+2):
        for j in range(c, c+2):
            res.append(graph[i][j])
    res.sort()
    return res[-2]

def make_array(graph, n):
    r_idx = 0
    c_idx = 0
    new_graph = [[0]*(n//2) for _ in range(n//2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            new_graph[r_idx][c_idx] = find_2nd(graph, i, j)
            c_idx += 1
        r_idx += 1
        c_idx = 0
    if len(new_graph) == 1:
        print(new_graph[0][0])
        exit()
    else:
        make_array(new_graph, n//2)
make_array(graph, n)