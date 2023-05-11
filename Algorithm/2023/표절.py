import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = 0
for i in range(N-1):
    start, end = i+1, N-1
    t = -1
    while start <= end:
        mid = (start+end)//2
        if lst[i] >= 0.9*lst[mid]:
            t = mid
            start = mid + 1
        else:
            end = mid - 1
    res += t-i if t > -1 else 0
print(res)