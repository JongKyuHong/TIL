import sys
input = sys.stdin.readline

N = int(input())
res = []
visited = [0] * (N+1)
def find(depth):
    if depth == N:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):
        if depth == 0:
            res.append(i)
            visited[i] = 1
            find(depth+1)
            res.pop()
            visited[i] = 0
        elif not visited[i]:
            res.append(i)
            visited[i] = 1
            find(depth+1)
            res.pop()
            visited[i] = 0

find(0)