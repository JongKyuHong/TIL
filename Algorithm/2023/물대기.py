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

N = int(input())
parent = [i for i in range(N+1)]

edges = []
for i in range(1, N+1):
    edges.append([int(input()), 0, i])
graph = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N):
    for j in range(i+1, N+1):
        edges.append([graph[i-1][j-1], i, j])
edges.sort()
res = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)
