import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

left, right = 0, max(lst)
ans = 0
while left <= right:
    mid = (left+right)//2
    tmp = 0
    for i in range(N):
        if mid > lst[i]:
            tmp += lst[i]
        else:
            tmp += mid
    if tmp > M:
        right = mid - 1
    elif tmp <= M:
        ans = max(ans, mid)
        left = mid + 1
print(ans)