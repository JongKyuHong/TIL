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

n, m = map(int, input().split()) # 학교수 학교를 연결하는 도로수
lst = list(input().rstrip().split())
edges = []
for _ in range(m):
    u, v, d = map(int, input().split()) # u학교, v학교, 거리 d
    edges.append((d,u,v))

parent = [i for i in range(n+1)]

edges.sort()
res = 0
cnt = 0
for cost, a, b in edges:
    if find(a) != find(b) and lst[a-1] != lst[b-1]:
        union(a, b)
        res += cost
        cnt += 1
if cnt == n-1:
    print(res)
else:
    print(-1)