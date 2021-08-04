import heapq

n,m = map(int,input().split())
state = list(map(int,input().split()))
heapq.heapify(state)
while m > 0:
    a = heapq.heappop(state)
    b = heapq.heappop(state)
    heapq.heappush(state,a+b)
    heapq.heappush(state,a+b)
    m -= 1
print(sum(state))