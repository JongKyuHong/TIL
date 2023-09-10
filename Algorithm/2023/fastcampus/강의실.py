import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    number, start, end = map(int, input().split())
    lst.append((start, end, number))
lst.sort(key=lambda x: x[0])

q = [] # heapq에 넣을건데 
for start, end, number in lst:
    if not q:
        heapq.heappush(q, end)
    else:
        flag = 0
        for i in range(len(q)):
            if q[i] <= start:
                q[i] = end
                flag = 1
                break
        if not flag:
            heapq.heappush(q, end)
print(len(q))
