import heapq

n = int(input())
array = []
for _ in range(n):
    deadline, cup = map(int,input().split())
    array.append((deadline,cup))
array.sort()
print(array)
queue = []
for i in array:
    heapq.heappush(queue,i[1])
    print(len(queue))
    if i[0] < len(queue):
        heapq.heappop(queue)
print(sum(queue))