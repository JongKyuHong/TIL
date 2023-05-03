import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    for i in range(min(N//2, M//2)):
        tmp = A[i][M-i-1] # 맨 오른쪽 상단
        for j in range(i, N-i-1):# ↑
            A[j][M-i-1] = A[j+1][M-i-1]
        A[N-i-1][i+1:M-i] = A[N-i-1][i:M-i-1]# ->
        for j in range(N-i-2, i-1, -1):# ↓
            A[j+1][i] = A[j][i]
        A[i][i:M-i-1] = A[i][i+1:M-i]# <-
        A[i][M-i-2] = tmp

for i in A:
    print(*i)
 
# 회전 횟수만큼 돌려준다
# 회전 알고리즘은 행과 열중 짧은것의 반나눔


