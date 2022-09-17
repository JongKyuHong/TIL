import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
visited = [0] * (N)
res = []
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(idx, N):
        if depth == 0:
            res.append(S[i])
            visited[i] = 1
            find(depth+1, i)
            visited[i] = 0
            res.pop()
        elif i > idx and not visited[i]:
            visited[i] = 1
            res.append(S[i])
            find(depth+1, i)
            res.pop()
            visited[i] = 0

find(0, 0)