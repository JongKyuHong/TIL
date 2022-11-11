import sys 
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
result = 0
graph.sort()
for g in graph:
    cost, a, b = g
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a, b)
        result += cost
print(result)