def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n+1)
graph = []

for i in range(n+1):
    parent[i] = i
    
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))
graph.sort()
last = 0
res = 0

for edge in graph:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        last = cost
print(res - last)
    