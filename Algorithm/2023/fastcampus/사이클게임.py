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

n, m = map(int, input().split())
parent = [i for i in range(n)]
flag = 1
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        flag = 0
        print(i+1)
        break
    else:
        union(a, b)
if flag:
    print(0)