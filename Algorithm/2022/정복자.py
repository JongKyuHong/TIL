import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m, t = map(int, input().split())
edges = []
ans = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1 or b == 1:
        ans.append((c,a,b))
    else:
        edges.append((c,a,b))

ans.sort()
a1 = ans[0]
edges = edges + ans[1:]
parent = [i for i in range(n+1)]
edges.sort()
edges = [a1]+edges
gap = 0
res = 0
for cost,a,b in edges:
    if find(a) != find(b):
        union(a,b)
        res += (cost+gap)
        gap += t
print(res)

