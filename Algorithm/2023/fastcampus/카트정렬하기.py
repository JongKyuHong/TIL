import heapq
import sys 
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    card = int(input())
    heapq.heappush(q, card)
result = 0
while 1:
    if len(q) == 1:
        break
    one, two = heapq.heappop(q), heapq.heappop(q)
    result += one+two
    heapq.heappush(q, one+two)
print(result)
