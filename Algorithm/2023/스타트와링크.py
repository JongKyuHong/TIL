import sys
input = sys.stdin.readline

def dfs(depth, index):
    global ans
    if depth == N//2:
        startSum = 0
        linkSum = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    startSum += graph[i][j]
                elif not visited[i] and not visited[j]:
                    linkSum += graph[i][j] 
        ans = min(ans, abs(startSum-linkSum))
        return            
            
    else:
        for i in range(index, N):
            if not visited[i]:
                visited[i] = 1
                dfs(depth+1, i+1)
                visited[i] = 0
N = int(input())
ans = float('inf')
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
dfs(0, 0)
print(ans)