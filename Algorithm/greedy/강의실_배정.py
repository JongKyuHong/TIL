import sys
import heapq
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(list(map(int,sys.stdin.readline().split())))
t = sorted(array,key=lambda x:x[0])

q = []

for i in t:
    print(type(q[0]))
    if q and q[0] <= i[0]:
        heapq.heappop(q)
    heapq.heappush(q,i[1])
print(len(q))
