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

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
edges = [] 
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((lst[i][j],i+1,j+1))

edges.sort()
res = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)