import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
left, right = 0, max(lst)*M
time = float('inf')
while left <= right:
    mid = (left+right)//2
    tmp = 0
    for i in lst:
        tmp += mid//i
    if tmp >= M:
        right = mid-1
        time = mid
    elif tmp < M:
        left = mid+1
print(time)
