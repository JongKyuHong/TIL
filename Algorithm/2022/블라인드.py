import sys 
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m*5+1)]
visited = [[0]*(n*5+1) for _ in range(m*5+1)]
count = [0]*5
for i in range(m*5+1):
    for j in range(n*5+1):
        if not visited[i][j]:
            if graph[i][j] == '.':
                for k in range(i, i+4):
                    for l in range(j, j+4):
                        visited[k][l] = 1
                count[0] += 1
            elif graph[i][j] == '*':
                cnt = 0
                for k in range(i, i+4):
                    if graph[k][j] == '*':
                        cnt += 1
                    for l in range(j, j+4):
                        visited[k][l] = 1
                count[cnt] += 1
print(*count)