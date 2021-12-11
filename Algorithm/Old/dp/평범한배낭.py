n,k = map(int,input().split())
array = [[0,0]]
for _ in range(n):
    array.append(list(map(int,input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = array[i][0]
        value = array[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],value+dp[i-1][j-weight])

print(dp[n][k])
#https://hongcoding.tistory.com/50        