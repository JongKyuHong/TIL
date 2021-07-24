import heapq
import sys

n,k = map(int,input().split())

gem = []
for _ in range(n):
    heapq.heappush(gem,map(int,sys.stdin.readline().split()))
bag = []
for _ in range(k):
    heapq.heappush(gem,map(int,sys.stdin.readline().split()))
print(gem)
