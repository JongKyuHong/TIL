import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    edges.append((a,b))

for edge in edges:
    a, b = edge
    if find(a) != find(b):
        union(a, b)

print(parent)
