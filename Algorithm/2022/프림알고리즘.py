def prim(start):
    visited = [0] * (n+1)
    visited[start] = 1
    distance = 0

    for _ in range(n+1):
        min_dist, next_node = float('inf'), -1

        for node in visited:
            for j in range(1, n+1):
                if j not in visited and 0 < graph[node][j] < min_dist:
                    min_dist = graph[node][j]
                    next_node = j
        distance += min_dist
        visited[next_node] = 1
    return distance

n, m = map(int, input().split())
graph = [[0 for i in range(n)] for _ in range(n+1)]

for _ in range(m):
    x, y, value = map(int, input().split())
    graph[x][y] = value
    graph[y][x] = value

print(prim(1))