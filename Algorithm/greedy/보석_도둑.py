import heapq

n,k = map(int,input().split())
array_j = []
for _ in range(n):
    heapq.heappush(array_j,list(map(int,input().split()))) # 무게, 가격

bags = []
for _ in range(k):
    heapq.heappush(bags,int(input()))

new_array = []
cnt = 0
for _ in range(k):
    bag = heapq.heappop(bags)
    print(bag)
    print(array_j)
    while array_j and bag >= array_j[0][0]:
        m,v = heapq.heappop(array_j)
        heapq.heappush(new_array,-v)
    if new_array:
        cnt -= heapq.heappop(new_array)
    elif not array_j:
        break
print(cnt)