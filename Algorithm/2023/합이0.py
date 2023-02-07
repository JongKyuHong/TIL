from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt_lst = Counter(lst)
ans = 0
for i in range(N-2):
    start = i+1
    end = N-1
    while start < end:
        if lst[start] + lst[end] + lst[i] == 0:
            if lst[start] == lst[end]:
                ans += end-start
            else:
                ans += cnt_lst[lst[end]]
            start += 1
        elif lst[start] + lst[end] + lst[i] > 0:
            end -= 1
        else:
            start += 1
print(ans)
