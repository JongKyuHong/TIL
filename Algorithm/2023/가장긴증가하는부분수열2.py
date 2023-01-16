import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [0]
for i in lst:
    if dp[-1] < i:
        dp.append(i) 
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (left+right)//2
            if dp[mid] < i:
                left = mid+1
            else:
                right = mid
        print(right, dp, i)
        dp[right] = i
print(dp)
print(len(dp)-1)