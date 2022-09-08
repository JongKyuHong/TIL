import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
# 같은수를 여러번 골라도 된다
# 고른 수열은 비내림차순
res = []
visited = [0] * N
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str,res)))
        return
    summary = 0
    for i in range(idx, N):
        if summary != S[i]:
            #visited[i] = 1
            res.append(S[i])
            summary = S[i]
            find(depth+1, i)
            res.pop()
            #visited[i] = 0
find(0, 0)
