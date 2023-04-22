import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if A[a] > A[b]:
            parent[a] = b
        else:
            parent[b] = a

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
for idx, root in enumerate(parent):
    if idx == root:
        ans += A[idx]
if ans <= k:
    print(ans)
else:
    print('Oh no')