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

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    edge = []
    for _ in range(M):
        a, b = map(int, input().split())
        edge.append((a,b))
    cnt = 0
    for a, b in edge:
        if find(a) != find(b):
            union(a, b)
            cnt += 1
    print(cnt)