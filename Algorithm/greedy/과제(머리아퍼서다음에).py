import heapq

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:(x[0],x[1]),reverse=True)


