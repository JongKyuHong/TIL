import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []
visited = [0] * (N+1)
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        if depth == 0:
            res.append(i)
            find(depth+1, i)
            res.pop()
        elif i >= idx:
            res.append(i)
            find(depth+1, i)
            res.pop()

find(0, 0)