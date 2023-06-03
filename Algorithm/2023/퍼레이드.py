import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node):
    for i in lst[node]:
        if not visited[i-1]:
            visited[i-1] = 1
            dfs(i)
V, E = map(int, input().split())
lst = [[] for _ in range(V+1)]
visited = [0 for i in range(V)]
adj = [0 for i in range(V)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a-1] += 1
    adj[b-1] += 1
    lst[a].append(b)
    lst[b].append(a)

odd = 0
for i in range(V):
    if adj[i] % 2 == 1:
        odd += 1

if odd == 1 or odd > 2:
    print("NO")
else:
    visited[0] = 1
    dfs(1)
    for elem in visited:
        if not elem:
            print("NO")
            exit()
    print("YES")