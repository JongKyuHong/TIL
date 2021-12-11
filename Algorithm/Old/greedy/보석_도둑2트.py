import heapq

n, k = list(map(int,input().split())) # 보석갯수, 가방갯수
gems = []
for _ in range(n):
    we, mo = list(map(int,input().split()))
    heapq.heappush(gems,[we,mo]) #보석정보 보석무게 가격
bags = []
for _ in range(k):
    cap = int(input())   # 가방이 수용할 수 있는 무게
    heapq.heappush(bags,cap)
gems.sort(key=lambda x:(x[1],x[0]),reverse=True)


total_value = 0
new_gems = []
for _ in range(k):
    cap = heapq.heappop(bags)
    while gems and cap >= gems[0][0]:
        w,v = heapq.heappop(gems)
        heapq.heappush(new_gems,-v)
    if new_gems:
        total_value -= heapq.heappop(new_gems)
    elif not gems:
        break
print(total_value)


