import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
visited = [0] * (N+1)
res = []
def find(depth):
    if depth == M:
        print(' '.join(map(str, res)))    
        return
    
    for i in range(N):
        if depth == 0 or not visited[i]:
            visited[i] = 1
            res.append(S[i])
            find(depth+1)  
            res.pop()
            visited[i] = 0

find(0)