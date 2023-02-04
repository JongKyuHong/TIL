import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    rows = []
    cols = []
    for i in range(N):
        rows.append(sum(array[i]))
    for i in range(N):
        v = 0
        for j in range(N):
            v += array[j][i]
        cols.append(v)

    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1-1,r2):
            rows[i] += (c2-(c1-1))*v
        for i in range(c1-1, c2):
            cols[i] += (r2-(r1-1))*v
    print(*rows)
    print(*cols)