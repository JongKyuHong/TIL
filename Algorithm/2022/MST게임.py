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

n, m, k = map(int, input().split())
edges = []
for i in range(1,m+1):
    x, y = map(int, input().split())
    edges.append((i, x, y))
edges.sort()

flag = 0
for i in range(k):
    if flag:
        print(0, end=' ')
    else:
        parent = [i for i in range(n+1)]
        cnt = 0
        res = 0
        for edge in edges[i:]:
            cost, a, b = edge
            if find(a) != find(b):
                union(a, b)
                res += cost
                cnt += 1
            if cnt == n-1:
                print(res, end=' ')
                break
        else:
            print(0, end=' ')
            flag = 1