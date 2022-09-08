import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
res = []

visited = [0] * (N+1)
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return 
    summary = 0
    for i in range(idx, N):
        if not visited[i] and summary != S[i]:
            res.append(S[i])
            visited[i] = 1
            summary = S[i]
            find(depth+1, i)
            res.pop()
            visited[i] = 0
find(0, 0)