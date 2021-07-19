import heapq

def solution(scoville,K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            heapq.heappush(scoville,heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            count += 1
        else:
            return -1
    return count

print(solution([1, 2, 3, 9, 10, 12],7))
