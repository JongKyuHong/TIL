import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
left, right = 0, N-1
ans = lst[left] + lst[right]
while left < right:
    tmp = lst[left] + lst[right]
    if abs(ans) > abs(tmp):
        ans = tmp
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(ans)