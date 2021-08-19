t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    dp = [0] * 31  # n의 최대값이 300이므로
    dp[1] = 1  # n이 1일때 나올수있는 블록의 갯수가 1
    dp[2] = 3  # n이 2일때 나올수있는 블록의 갯수가 3
    for i in range(3,(n//10)+1):  
        # 맨뒤에 10x20이 들어온경우가 하나 20x20이 들어온경우가 하나, 20x10이 두개가 들어온경우가 하나
        # 20x10이 2개면 사실상 20x20이랑 같으므로 곱하기 2를함 즉 dp[n]을 만들기에
        # dp[n-1]은 하나 dp[n-2]는 두개가가 들어올수있어 dp[n] = dp[i-1] + 2*dp[i-2]
        dp[i] = dp[i-1] + 2*dp[i-2]  
    print(f'#{test_case}',max(dp))
