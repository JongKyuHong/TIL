import sys
input = sys.stdin.readline
 
n, m, r = map(int, input().split()) # 수행해야 하는 회전의 수 r
A = [list(map(int, input().split())) for _ in range(n)]



for _ in range(r):
    start_r, start_c, end_r, end_c = 0, 0, n-1, m-1
    while  start_r < end_r and start_c < end_c:
        prev = 0
        for i in range(end_c, start_c, -1): # 열
            if i == end_c:
                prev = A[start_r][i-1]
                A[start_r][i-1] = A[start_r][i]
            else:
                prev2 = A[start_r][i-1]
                A[start_r][i-1] = prev
                prev = prev2

        prev2 = 0
        for i in range(start_r+1, end_r):
            if i == start_r+1:
                prev2 = A[i+1][start_c]
                A[i+1][start_c] = A[i][start_c]
                A[i][start_c] = prev
            else:
                prev = A[i+1][start_c]
                A[i+1][start_c] = prev2
                prev2 = prev

        for i in range(start_c+1, end_c):
            if i == start_c+1:
                prev2 = A[end_r][i+1]
                A[end_r][i+1] = A[end_r][i]
                A[end_r][i] = prev
            else:
                prev = A[end_r][i+1]
                A[end_r][i+1] = prev2
                prev2 = prev

        for i in range(end_r-1,start_r,-1):
            if i == end_r-1:
                prev2 = A[i-1][end_c]
                A[i-1][end_c] = A[i][end_c]
                A[i][end_c] = prev
            else:
                prev = A[i-1][end_c]
                A[i-1][end_c] = prev2
                prev2 = prev

        start_r += 1
        start_c += 1
        end_r -= 1
        end_c -= 1

for i in A:
    print(i)



