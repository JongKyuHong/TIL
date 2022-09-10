import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
res = []
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(N):
        if depth == 0:
            res.append(S[i])
            find(depth+1, i)
            res.pop()
        elif i >= idx:
            res.append(S[i])
            find(depth+1, i)
            res.pop()

find(0, 0)