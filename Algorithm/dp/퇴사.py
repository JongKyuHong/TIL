n = int(input())
array = [ list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
max_d = 0
for i in range(1,n+1):
    dp[i] = max(dp[i-1], max_d)
    if dp[i] > max_d:
        max_d = dp[i]

#https://jrc-park.tistory.com/119?category=378936

