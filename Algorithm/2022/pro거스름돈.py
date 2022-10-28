# from itertools import combinations_with_replacement, permutations, combinations
# def solution(n, money):
#     answer = 0
#     money.sort()
#     for i in range(1, (n//money[0])+1):
#         for c in combinations_with_replacement(money, i):
#             if sum(c) == n:
#                 answer += 1
#     return answer%1000000007

#print(solution(5,[1,2,5]))

# from collections import deque
# def solution(n, money):
#     answer = 0
#     res = []
#     #money.sort()
#     for i in range(len(money)):
#         q = deque([[money[i], 1,[money[i]]]])
#         while q:
#             m, cnt,path = q.popleft()
#             if m == n and cnt not in res:
#                 answer += 1
#                 res.append(cnt)
#                 print(path)
#             elif m < n:
#                 for j in range(len(money)):
#                     q.append((money[j]+m, cnt+1,path+[money[j]]))
#         answer %= 1000000007
#     return answer%1000000007

def solution(n, money):
    dp = [1] + [0]*n
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                dp[i] += dp[i-m]
    return dp[n]%1000000007

# 1

# 1 1
# 2

# 1 1 1
# 1 2

# 1 1 1 1
# 1 1 2
# 2 2

# 1 1 1 1 1
# 1 1 1 2
# 1 2 2 
# 5 ,,, 1추가

# 1 1 1 1 1 1 
# 1 1 1 1 2
# 1 1 2 2
# 1 5
# 2 2 2

print(solution(5, [1,2,5]))
#print(solution(6, [1,2,5]))
#print(solution(150, [150,20,18]))
#print(solution(800,[100,400,500]))