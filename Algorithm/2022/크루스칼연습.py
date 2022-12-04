import sys
input = sys.stdin.readline

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i
res = 0

for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a, b)
        res += c
print(res)
