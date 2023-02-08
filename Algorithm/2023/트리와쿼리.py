import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

size = [0]*(N+1)
visited = [0]*(N+1)
visited[R] = 1
def maketree(node):
    size[node] = 1
    for i in tree[node]:
        if not visited[i]:
            visited[i] = 1
            maketree(i)
            size[node] += size[i]

maketree(R)
for _ in range(Q):
    U = int(input())
    print(size[U])
