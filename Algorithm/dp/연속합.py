n = int(input())
array = list(map(int,input().split()))
result = -1001
dp = [0 for _ in range(n)]
for i in range(n):
    # dp이전값과 array[i]를 더한값이 array[i]보다 작으면 걔를 껴서 더할 이유가없으므로 max를 써서 그값을 버림
    dp[i] = max(dp[i-1] + array[i],array[i])  
    result = max(result,dp[i])
print(result)