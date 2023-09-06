import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
nums = list(map(int, input().split()))
for num in nums:
    start, end = 0, N-1
    flag = 0
    while start <= end:
        mid = (start+end)//2
        if lst[mid] > num:
            end = mid - 1
        elif lst[mid] < num:
            start = mid + 1
        else:
            flag = 1
            break
    if not flag:
        print(0)
    else:
        print(1)