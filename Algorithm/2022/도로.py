import sys
input = sys.stdin.readline

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(int(input())):
    n,m,p,q = map(int, input().split()) # n은 도시수, m은 길이수, p와q는 확인해야할 도로
    edges = []
    res = []
    for _ in range(m):
        u,v,w = map(int, input().split())
        if (u == p and v == q) or (v==p and u==q):
            res.append((w,u,v))
        else:
            edges.append((w,u,v))
    parent = [i for i in range(n+1)]
    edges.sort()
    edges = res + edges
    ans = 0
    for edge in edges:
        cost, a, b = edge
        if find(a) != find(b):
            union(a, b)
            ans += cost
    
    parent = [i for i in range(n+1)]
    #edges.sort()
    #edges = res + edges
    edges.sort()
    ans2 = 0
    for edge in edges:
        cost, a, b = edge
        if find(a) != find(b):
            union(a, b)
            ans2 += cost
    if ans2 == ans:
        print('YES')
    else:
        print('NO')
