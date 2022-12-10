import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def carculate(c1, c2):
    return min(abs(c1[0]-c2[0]),abs(c1[1]-c2[1]),abs(c1[2]-c2[2]))

min_v = float('inf')
n = int(input())
coordinate = []
for i in range(1,n+1):
    x,y,z = map(int, input().split())
    coordinate.append((x,y,z,i))
edges = []
parent = [i for i in range(n+1)]
for i in range(3):
    coor = sorted(coordinate, key=lambda x : x[i])
    for j in range(n-1):
        edges.append((abs(coor[j][i]-coor[j+1][i]),coor[j][3],coor[j+1][3]))
edges.sort()
res = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)