import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# s~e가 팰린드롬인지 판단하려면 lst[s] == lst[e]인지를 먼저 판단
# 내부의 lst[s+1][e-1]이 팰린드롬인지 판단한다.
# 우선 홀수인경우 모두 1
# 2까지 짝수인경우 둘이 같으면 1

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N): # 시작점에서 얼마나 떨어져있는지
    for j in range(N): # 이게 기준 시작점
        if i < j:
            continue
        elif i == j:
            dp[i][j] = 1
        else:
            if i-j == 1:
                if lst[i] == lst[j]:
                    dp[j][i] = 1
                else:
                    dp[j][i] = 0
            else:
                if lst[i] == lst[j]:
                    if dp[j+1][i-1] == 1:
                        dp[j][i] = 1
                    else:
                        dp[j][i] = 0
                else:
                    dp[i][j] = 0
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
