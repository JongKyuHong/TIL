# import heapq

# def solution(jobs):
#     answer,now,i = 0,0,0
#     start = -1
#     heap = []

#     while i < len(jobs):
#         for j in jobs:
#             if start < j[0] <= now:
#                 heapq.heappush(heap,[j[1],j[0]])
#         if len(heap) > 0:
#             current = heapq.heappop(heap)
#             start = now
#             now += current[0]
#             answer += (now - current[1])
#             i += 1
#         else:
#             now += 1
#     return int(answer/len(jobs))

# #jobs [작업이 요청되는 시점, 작업의 소요시간]
# jobs = [[0, 3], [1, 9], [2, 6]]
# solution(jobs)
