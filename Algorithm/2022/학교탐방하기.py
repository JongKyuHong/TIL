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


n, m = map(int, input().split())
edges = []
start = []
for _ in range(m+1):
    a, b, c = map(int, input().split()) # a와b건물 c는 0(오르막길) 1(내리막길)
    if a == 0:
        start.append((c,a,b))
    else:
        edges.append((c,a,b))

res = []
for i in range(2):
    if i == 0:
        edges.sort()
    else:
        edges.sort(reverse=True)
    edge = start+edges
    parent = [i for i in range(n+1)]
    cnt = 0
    for cost, a, b in edge:
        if find(a) != find(b):
            if cost == 0:
                cnt += 1
            union(a, b)
    res.append(cnt)
res.sort(reverse=True)
print(res[0]**2 - res[1]**2)