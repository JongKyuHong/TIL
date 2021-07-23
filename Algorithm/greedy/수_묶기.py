import heapq

T = int(input())
array = []
for _ in range(T):
    heapq.heappush(array,int(input()))
answer = 0
i = 0 
if len(array)%2:
    print(array)
    exit(0)
    while len(array) > 1:
        element = heapq.heappop(array)
        element2 = heapq.heappop(array)
        if i == 0 and element <= 0 and element2 <= 0:
            answer += element*element2
        elif i == 0 and element < 0 and element2 > 0:
            answer += element
            element = heapq.heappop(array)
        if (element <  0 and element2 > 0) or (element > 0 and element2 < 0):
            answer += element+element2
        elif (element < 0 and element2 == 0) or (element == 0 and element2 < 0):
            answer += element*element2
        else:
            answer += element*element2
        i += 1
else:
    while len(array) > 1:
        element = heapq.heappop(array)
        element2 = heapq.heappop(array)
        if element*element2 < 0:
            answer += element+element2
        else:
            answer += element*element2

if len(array) >= 1:
    answer += heapq.heappop(array)
print(answer)
