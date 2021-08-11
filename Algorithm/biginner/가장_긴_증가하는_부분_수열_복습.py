n = int(input())
a = list(map(int,input().split()))
# dp = [1 for i in range(n)] # 길이를 담아야하기때문에 1로 초기화한 dp리스트 생성
# for i in range(n):  # a를 순회하기 위한 for문
#     for j in range(i):  # i보다 인덱스값이 작은것들과 크기비교위함
#         if a[i] > a[j]:  # 새로운 위치가 전에보다 크면
#             dp[i] = max(dp[i],dp[j]+1)  # dp[i]값을 정함
# print(max(dp))

dp = [0 for i in range(n)]
dp[0] = a[0]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j]+a[i])
            print(dp[i])
        else:
            dp[i] = max(dp[i],a[i])
print(dp)