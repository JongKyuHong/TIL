import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 1000000001
ans = 0
while left <= right:
    mid = (left+right)//2
    val = 0
    for i in lst:
        if i > mid:
            val += i - mid
    if val >= M:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1
    
print(ans)
