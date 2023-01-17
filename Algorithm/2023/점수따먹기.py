import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] 
S = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + graph[i-1][j-1]
ans = -float('inf')
for i in range(1, N+1):
    for j in range(1, M+1):
        for x1 in range(i, N+1):
            for y1 in range(j, M+1):
                ans = max(ans, S[x1][y1] - S[x1][j-1] - S[i-1][y1] + S[i-1][j-1])
print(ans)

