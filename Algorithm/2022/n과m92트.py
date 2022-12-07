import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
res = []
visited = [0] * N
def find(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    
    tmp = 0
    for i in range(N):
        if tmp != S[i] and not visited[i]:
            visited[i] = 1
            res.append(S[i])
            tmp = S[i]
            find(depth+1)
            visited[i] = 0
            res.pop()
find(0)