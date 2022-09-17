import heapq

n = int(input())
Xlist = [int(input()) for _ in range(n)]

array = []

for X in Xlist:
    if X:
        heapq.heappush(array,X)
    elif X == 0:
        if array:
            print(heapq.heappop(array))
        else:
            print(0)
