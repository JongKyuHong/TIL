import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
visited = [0] * N
res = []
def find(depth, idx):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    tmp = 0
    for i in range(N):
        # if depth == 0 and tmp != S[i]:
        #     visited[i] = 1
        #     res.append(S[i])
        #     tmp = S[i]
        #     find(depth+1, i)
        #     res.pop()
        #     visited[i] = 0
        #el
        if tmp != S[i] and not visited[i] and i > idx:
            visited[i] = 1
            res.append(S[i])
            tmp = S[i]
            find(depth+1, i)
            res.pop()
            visited[i] = 0
find(0, -1)