import heapq
import sys
input = sys.stdin.readline

N = int(input())
left, right = [], []
middle = int(input())
print(middle)
for i in range(1, N):
    inp = int(input())
    if inp > middle:
        heapq.heappush(right, inp)
    else:
        heapq.heappush(left, -inp)
    if len(left) < len(right):
        rv = heapq.heappop(right)
        if i % 2:
            heapq.heappush(left, -middle)
            print(middle)
            middle = rv
        else:
            heapq.heappush(left, -middle)
            print(rv)
            middle = rv
    elif len(left) > len(right):
        lv = -heapq.heappop(left)
        heapq.heappush(right, middle)
        print(lv)
        middle = lv
    else:
        print(middle)
