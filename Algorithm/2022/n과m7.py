import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
res = []
def find(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(N):
        res.append(S[i])
        find(depth+1)
        res.pop()
find(0)