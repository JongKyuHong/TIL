n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n
dp2 = [1] * n
prev = numbers[0]
#prev2 = numbers[0]
for i in range(1,n):
    if prev <= numbers[i]:
        dp[i] = dp[i-1] + 1
    if prev >= numbers[i]:
        dp2[i] = dp2[i-1] + 1
    prev = numbers[i]

print(max(max(dp),max(dp2)))


