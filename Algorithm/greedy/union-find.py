N =int(input())
M = int(input())
parent = [0] * (N+1)
rank = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a== b:
        return 
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] +=1