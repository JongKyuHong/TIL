import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [0] * (N+1)
visited = [0]*(N+1)
res = []
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(idx, N+1):
        if depth == 0 or not visited[i]:
            visited[i] = 1
            res.append(i)
            find(depth+1, i)
            res.pop()
            visited[i] = 0

find(0, 1)