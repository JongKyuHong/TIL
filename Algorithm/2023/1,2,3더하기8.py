import sys
input = sys.stdin.readline

T = int(input())
max_n = 0
nums = []
for _ in range(T):
    n = int(input())
    max_n = max(max_n, n)
    nums.append(n)
dp = [[0]*(2) for _ in range(max_n+1)]
if max_n >= 1:
    dp[1][0] = 1 # 1
    dp[1][1] = 0 # 0
if max_n >= 2:
    dp[2][0] = 1 # 2
    dp[2][1] = 1 # 11
if max_n >= 3:
    dp[3][0] = 2 # 111 3
    dp[3][1] = 2 # 21 12
    for i in range(4, max_n+1):
        dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1])%1000000009
        dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0])%1000000009
    for num in nums:
        print(dp[num][0], dp[num][1])

# lst = []
# odd_lst = []
# even_lst = []
# nums1 = ['1','2','3']
# target_nums = 8
# def dfs(value, string):
#     global target_nums
#     if value > target_nums:
#         return
#     elif value == target_nums:
#         if string not in lst:
#             lst.append(string)
#             if len(string) % 2:
#                 odd_lst.append(string)
#             else:
#                 even_lst.append(string)
#         return
#     for i in range(3):
#         dfs(value+int(nums1[i]), string+nums1[i])
#         dfs(value+int(nums1[i]), nums1[i]+string)

# for i in range(3):
#     dfs(int(nums1[i]), nums1[i])