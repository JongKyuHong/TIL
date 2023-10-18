import heapq
import sys 
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(1, N+1):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort()
q = []
for i in lst:
    a = i[0]
    heapq.heappush(q, i[1])
    print(q,'qq')
    if a < len(q):
        heapq.heappop(q)
    print(q,'qq2')
print(sum(q))