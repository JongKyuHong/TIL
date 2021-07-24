import heapq
import sys

n,k = map(int,input().split())

gem = []
for _ in range(n):
    weight,value = map(int,sys.stdin.readline().split())
    heapq.heappush(gem,[weight,value])
bag = []
for _ in range(k):
    capacity = int(sys.stdin.readline())
    heapq.heappush(gem,capacity)
total_value = 0
capable_gem = []
for _ in range(k):
    capacity = heapq.heappop(bag)
    while gem and capacity >= gem[0][0]:
        weight,value = heapq.heappop(gem)
        heapq.heappush(capable_gem,-value)
    if capable_gem:
        total_value -= heapq.heappop(capable_gem)
    elif not gem:
        break
print(total_value)
