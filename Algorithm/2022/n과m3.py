import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N+1)
res = []
def find(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1,N+1):
        res.append(i)
        find(depth+1)
        res.pop()

find(0)
# for i in range(1, N+1):
#     res.append(i)
#     find(1)
#     res.pop()