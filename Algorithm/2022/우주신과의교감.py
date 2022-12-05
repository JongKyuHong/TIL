import sys
import math
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

def carculate_dist(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

n, m = map(int, input().split()) # 우주신의 갯수, 연결된 신들과의 통로의 갯수
coordinate = []
parent = [i for i in range(n+1)]
for i in range(n):
    x, y = map(int, input().split())
    coordinate.append((x,y))

for i in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((carculate_dist(coordinate[i], coordinate[j]), i, j))

edges.sort()
res = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost
print('%.2f' % res)