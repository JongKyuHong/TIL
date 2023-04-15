import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
# 회전
# 대칭
for i in range(8):
    if i == 0:
        delta = ((0, 3), (0, -3), (3, 0), (-3, 0))
        for r in range(N):
            for c in range(M):
                for dr, dc in delta:
                    nr, nc = dr+r, dc+c
                    val = 0
                    if 0 <= nr < N and 0 <= nc < M:
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                    max_v = max(max_v, val)
    elif i == 1:
        delta = ((1, 1), (1, -1),(-1, 1),(-1, -1))
        for r in range(N):
            for c in range(M):
                for dr, dc in delta:
                    nr, nc = dr+r, dc+c
                    val = 0
                    if 0 <= nr < N and 0 <= nc < M:
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                    max_v = max(max_v, val)
    elif i == 2:
        delta = ((2, 1), (1, -2), (-2, -1), (-1, 2))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r][c+1] + lst[r+1][c+1])
                        elif j == 1:
                            val -= (lst[r+1][c] + lst[r+1][c-1])
                        elif j == 2:
                            val -= (lst[r][c-1] + lst[r-1][c-1])
                        else:
                            val -= (lst[r-1][c] + lst[r-1][c+1])
                        max_v = max(max_v, val)
    elif i == 3:
        delta = ((2, 1), (1, -2), (-2, -1), (-1, 2))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r][c+1] + lst[r+2][c])
                        elif j == 1:
                            val -= (lst[r+1][c] + lst[r][c-2])
                        elif j == 2:
                            val -= (lst[r][c-1] + lst[r-2][c])
                        else:
                            val -= (lst[r-1][c] + lst[r][c+2])
                        max_v = max(max_v, val)
    elif i == 4:
        delta = ((1, 2), (2, -1), (-1, -2), (-2, 1))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r+1][c] + lst[r+1][c+2])
                        elif j == 1:
                            val -= (lst[r][c-1] + lst[r+2][c-1])
                        elif j == 2:
                            val -= (lst[r-1][c] + lst[r-1][c-2])
                        else:
                            val -= (lst[r][c+1] + lst[r-2][c+1])
                        max_v = max(max_v, val)
    elif i == 5:
        delta = ((2, -1), (-1, -2), (-2, 1), (1, 2))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r][c-1] + lst[r+1][c-1])
                        elif j == 1:
                            val -= (lst[r-1][c-1] + lst[r-1][c])
                        elif j == 2:
                            val -= (lst[r-1][c+1] + lst[r][c+1])
                        else:
                            val -= (lst[r+1][c] + lst[r+1][c+1])
                        max_v = max(max_v, val)
    elif i == 6:
        delta = ((2, -1), (-1, -2), (-2, 1), (1, 2))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r][c-1] + lst[r+2][c])
                        elif j == 1:
                            val -= (lst[r-1][c] + lst[r][c-2])
                        elif j == 2:
                            val -= (lst[r][c+1] + lst[r-2][c])
                        else:
                            val -= (lst[r+1][c] + lst[r][c+2])
                        max_v = max(max_v, val)
    else:
        delta = ((1, -2), (-2, -1), (-1, 2), (2, 1))
        for r in range(N):
            for c in range(M):
                for j in range(4):
                    nr, nc = delta[j][0]+r, delta[j][1]+c
                    if 0 <= nr < N and 0 <= nc < M:
                        val = 0
                        if r > nr:
                            for r1 in range(nr, r+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        else:
                            for r1 in range(r, nr+1):
                                if c > nc:
                                    for c1 in range(nc, c+1):
                                        val += lst[r1][c1]
                                else:
                                    for c1 in range(c, nc+1):
                                        val += lst[r1][c1]
                        if j == 0:
                            val -= (lst[r+1][c] + lst[r+1][c-2])
                        elif j == 1:
                            val -= (lst[r][c-1] + lst[r-1][c-1])
                        elif j == 2:
                            val -= (lst[r-1][c] + lst[r-1][c+2])
                        else:
                            val -= (lst[r][c+1] + lst[r+2][c+1])
                        max_v = max(max_v, val)
print(max_v)
