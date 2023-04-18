import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) != find(c):
            print("NO")
        else:
            print("YES")