n = int(input())
graph = [list(input().split()) for _ in range(n)]

graph = sorted(graph, key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in graph:
    print(i[0])

