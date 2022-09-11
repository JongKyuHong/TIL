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
    tmp = 0
    for i in range(N):
        if depth == 0 and tmp != S[i]:
            res.append(S[i])
            tmp = S[i]
            find(depth+1)
            res.pop()
        elif tmp != S[i]:
            res.append(S[i])
            tmp = S[i]
            find(depth+1)
            res.pop()
find(0)