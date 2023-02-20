import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
graph = []
for _ in range(M):
    graph.append(list(input().rstrip()))

S = [[[0,0,0] for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        t = [0, 0, 0] 
        if graph[i-1][j-1] == 'J':
            t[0] += 1
        elif graph[i-1][j-1] == 'O':
            t[1] += 1
        elif graph[i-1][j-1] == 'I':
            t[2] += 1
        S[i][j][0] = S[i][j-1][0] + S[i-1][j][0] - S[i-1][j-1][0] + t[0]
        S[i][j][1] = S[i][j-1][1] + S[i-1][j][1] - S[i-1][j-1][1] + t[1]
        S[i][j][2] = S[i][j-1][2] + S[i-1][j][2] - S[i-1][j-1][2] + t[2]

for i in S:
    print(i)

for _ in range(K):
    a, b, c, d = map(int, input().split())
    a, b = a-1, b-1
    t = []
    t.append(S[c][d][0] - S[c][b][0] - S[a][d][0] + S[a][b][0])
    t.append(S[c][d][1] - S[c][b][1] - S[a][d][1] + S[a][b][1])
    t.append(S[c][d][2] - S[c][b][2] - S[a][d][2] + S[a][b][2])
    print(*t)


