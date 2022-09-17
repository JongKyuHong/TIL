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
    
    tmp = 0
    for i in range(N):
        if tmp != S[i] and i >= idx: 
            res.append(S[i])
            tmp = S[i]
            find(depth+1, i)
            res.pop()

find(0, -1)