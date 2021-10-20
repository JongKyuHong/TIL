from collections import deque

n, m, v = map(int, input().split())
array = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = array[a][b] = 1
visit_list = [0]*(n+1)


def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit_list[i] == 1 and array[v][i] == 1:
                q.append(i)
                visit_list[i] = 0

def dfs(v):
    visit_list[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if visit_list[i]==0 and array[v][i] == 1:
            dfs(i)


dfs(v)
print()
bfs(v)
