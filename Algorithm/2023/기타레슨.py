import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
left, right = 0, 100000*10000
result = sum(lst)

while left <= right:
    mid = (left+right)//2
    if mid < max(lst):
        left = mid + 1
        continue
    cnt, tmp = 1, 0
    for i in range(len(lst)):
        if tmp + lst[i] <= mid:
            tmp += lst[i]
        else:
            tmp = lst[i]
            cnt += 1
    
    if cnt <= M:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1
print(result)
