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

while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    parent = [-1]*(m+1)
    result = 0
    for i in range(m+1):
        parent[i] = i
    value = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        edges.append((c,a,b))
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(a, b)
            result += cost
        else:
            value += cost
    print(value)