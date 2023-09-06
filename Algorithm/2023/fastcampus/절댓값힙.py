import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x == 0: # 절댓값이 가장 작은 값을 제거
        if not q:
            print(0)
        else:
            abs_value, value = heapq.heappop(q)
            print(value)
    else:
        # 가장 작은 값이 위로 올라온다.
        heapq.heappush(q, [abs(x), x])