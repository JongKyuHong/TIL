import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
dp = [0]  
for i in a:
    if dp[-1] < i:  # a배열의 값이 dp맨위보다 크면
        dp.append(i)  # 그냥 dp위에 넣어버림
    else:  # 그렇지않다 dp값이 더크다 하면
        left= 0
        right = len(dp)
        while left < right:  # 이진탐색 간다.
            mid = (left+right)//2
            if dp[mid] < i:  # dp안쪽에 넣어주기위해 위치를 찾아준다.
                left = mid+1
            else:
                right = mid
        dp[right] = i
print(len(dp)-1) # 처음에 넣은 1값을 제외하기위해


