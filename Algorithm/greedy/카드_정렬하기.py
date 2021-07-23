import heapq

n = int(input())
money = []
for _ in range(n):
    heapq.heappush(money,int(input()))

if len(money) == 1:
    print(0)
else:
    answer = 0
    while len(money)>1:
        card1 = heapq.heappop(money)
        card2 = heapq.heappop(money)
        answer += card1+card2
        heapq.heappush(money,card1+card2)
print(answer)