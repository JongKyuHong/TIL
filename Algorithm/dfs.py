def dfs(s,v):
    visited = [0] *(v+1)
    stack = []
    visited[s] = 1
    i = s  # 현재 방문한 정점 i
    print(node[i])
    while i!=0:
        for w in range(1,v+1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0

node = ['','A','B','C','D','E','F','G']
v,e = map(int,input().split())
adj = [[0]*(v+1) for _ in range(v+1)]
for _ in range(e):
    n1, n2 = map(int,input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 연결되어있는 애들끼리 1


