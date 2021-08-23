import heapq

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
que = []
heapq.heappush(que, array[0][1])
for i in range(1,n):
    if que[0] > array[i][1]:
        heapq.heappush(que,array[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, array[i][1])
print(len(array))