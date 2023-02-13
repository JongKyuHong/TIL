import sys
input = sys.stdin.readline

def check(idx, cnt):
    global result
    if idx == N:
        result = max(result, cnt)
        print(result)
        exit()
        return
    else:
        for next_idx in range(idx+1, N, 2):
            if dp[idx][next_idx]:
                check(next_idx+1, cnt+1)

N = int(input())
A = list(map(int, input().split()))

dp = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in range(N-1):
    if A[i] == A[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):
    for j in range(N-i):
        if A[j] == A[j+1] and dp[j+1][j+i-1]:
            dp[j][j+1] = 1

max_num = N//2
result = -1
check(0, 0)
print(result)
