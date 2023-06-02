import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
if N % 2: # 홀수라면
    start, end = 0, N-1
    ans = 0
    while start < end:
        ans += lst[end] * 2
        start += 1
        end -= 1
    ans += lst[start]
    print(ans)
else:
    start, end = 0, N-1
    ans = 0
    while start < end:
        ans += lst[end] * 2
        start += 1
        end -= 1
    print(ans)