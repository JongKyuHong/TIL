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

v, e = map(int, input().split())
edges = []
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a, b, value = map(int, input().split())
    edges.append((value, a, b))

edges.sort()
res = 0
for a, b, value in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += value

print(res)
