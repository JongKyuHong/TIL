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

n, m, k = map(int, input().split())
powerplant = list(map(int, input().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

parent = [0]*(n+1)
for i in range(n+1):
    if i in powerplant:
        parent[i] = 0
    else:
        parent[i] = i
edges.sort()
res = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)
