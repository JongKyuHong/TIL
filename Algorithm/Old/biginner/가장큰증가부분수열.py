n = int(input())
a = list(map(int,input().split()))

dp = [i for i in a] # dp초기화
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:  # 자기보다 앞에있는 값중에 자기보다 작은 수를 찾으면
            dp[i] = max(dp[i],dp[j]+a[i])  # dp값을 정한다.
        # else:
        #     dp[i] = max(dp[i],a[i])  # 자기보다 크면 dp값과 자기자신을 비교해서 dp에 넣는다.
print(max(dp))