from itertools import permutations
from copy import deepcopy
import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]
ans = float('inf')

for p in permutations(rcs, K):
    copy_A = deepcopy(A)
    for r, c, s in p:
        r -= 1; c -= 1
        for n in range(s, 0, -1):
            tmp = copy_A[r-n][c+n]
            copy_A[r-n][c-n+1:c+n+1] = copy_A[r-n][c-n:c+n] # ->
            for row in range(r-n, r+n):  # ↑
                copy_A[row][c-n] = copy_A[row+1][c-n]
            copy_A[r+n][c-n:c+n] = copy_A[r+n][c-n+1:c+n+1]  # <-
            for row in range(r+n, r-n, -1):  # ↓
                copy_A[row][c+n] = copy_A[row-1][c+n]
            copy_A[r-n+1][c+n] = tmp

    # 3. 각 행의 최소값 찾기
    for row in copy_A:
        ans = min(ans, sum(row))
print(ans)

# 배열 돌리는법