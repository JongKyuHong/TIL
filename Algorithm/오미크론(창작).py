t = int(input())

for test_case in range(1, t+1):
    n ,d ,v = map(int, input().split())
    dp = [0] * (n+1)
    dp[0] = 10
    
    for i in range(1, n+1):
        if d <= i < v:
            dp[i] = dp[i-1] + i
        elif v <= i:
            dp[i] = dp[i-1] + (1/2 * i)
        else:
            dp[i] = dp[i-1] + (2 * i)
    print(f"#{test_case} {int(dp[n])}")