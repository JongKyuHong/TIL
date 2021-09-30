from collections import deque

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
for _ in range(m):
    a, b, c = map(int, input().split()) # a번집과 b번집을 연결하는 길의 유지비 c
    edges.append((c, a, b))

edges.sort()
result = 0
last = 0

for edge in edges:
    c, a, b = edge
    if get_parent(parent, a) != get_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c
print(result-last)

