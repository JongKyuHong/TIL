import sys
input = sys.stdin.readline

def dfs(prev, node):
    visited[node] = 1
    for n in tree[node]:
        if n == prev:
            continue
        if visited[n]:
            return 0
        if not dfs(node, n):
            return 0
    return 1

idx = 1
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tree = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    cycle = 0
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    cnt = 0
    for v in range(1, n+1):
        if not visited[v]:
            if dfs(0, v):
                cnt += 1
    
    if cnt == 0:
        print(f'Case {idx}: No trees.')
    elif cnt == 1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {cnt} trees.')
    idx += 1