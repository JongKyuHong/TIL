import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    lst = list(map(int, input().split()))
    heapq.heapify(lst)
    ans = 0
    while lst:
        if len(lst) == 1:
            print(ans)
            break
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        ans += (a+b)
        heapq.heappush(lst, a+b)