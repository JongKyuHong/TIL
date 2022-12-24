import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split()) # 정점의 갯수, 간선의 개수
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    if c >= 0:
        edges.append((c,a,b))
parent = [i for i in range(v+1)]
edges.sort()

res = 0
for c,a,b in edges:
    if find(a) != find(b):
        union(a, b)
        res += c
print(res)