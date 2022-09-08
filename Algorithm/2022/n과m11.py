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
    summary = 0
    for i in range(N):
        if summary != S[i]:
            res.append(S[i])
            summary = S[i]
            find(depth+1)
            res.pop()
           

find(0)