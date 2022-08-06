graph = []
max_v = 0
for i in range(5):
    data = input()
    data2 = list(data)
    max_v = max(max_v, len(data2))
    graph.append(data)

for i in range(max_v):
    for j in range(5):
        if i < len(graph[j]):
            print(graph[j][i],end='')
