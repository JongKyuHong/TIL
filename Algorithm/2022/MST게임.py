import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m, k = map(int, input().split())
edges = []

for i in range(1,m+1):
    a, b = map(int, input().split())
    edges.append((i,a,b))

for i in range(k):
    parent = [i for i in range(n+1)]
    res = 0
    cnt = 0
    for cost, a, b in edges[i:]:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            res += cost
            cnt += 1
        if cnt == n-1:
            print(res, end=' ')
            break
    else:
        print(0, end=' ')

