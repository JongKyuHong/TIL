# for test_case in range(int(input())):
#     n = int(input())
#     test_list = [list(map(int, input().split())) for _ in range(n)]
#     memo = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == 0:
#                 memo[i][j] = test_list[i][j]*0.01
#             else:
#                 for k in range(n):
#                     if j == k:
#                         continue
#                     else:
#                         if not memo[i][j] and memo[i-1][k] != 0:
#                             memo[i][j] = memo[i-1][k] * test_list[i][j]*0.01
#                         else:
#                             memo[i][j] = max(memo[i][j], memo[i-1][k]*test_list[i][j])*0.01
#     res = max(memo[n-1])
#     print(f'#{test_case+1} {res*100:.6f}')

def dfs(index, res):
    if index == n:
        global result
        if result < res:
            result = res
        return
    if res < result:
        return 
    for j in range(n):
        if not visited[j] and test_list[index][j] !=0:
            visited[j] = 1
            res2 = res*(test_list[index][j]*0.01)
            dfs(index+1, res2)
            visited[j] = 0


for test_case in range(int(input())):
    n = int(input())
    test_list = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    result = 0
    dfs(0, 1)
    print(f'#{test_case+1} {result*100:.6f}')
