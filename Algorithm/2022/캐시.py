# from collections import deque

# def solution(cacheSize, cities):
#     answer = deque([])
#     time = 0
#     idx = 0
#     if cacheSize == 0:
#         return len(cities)*5
#     else:
#         for i in cities:
#             i = i.lower()
#             idx += 1
#             if idx <= cacheSize:
#                 answer.append(i)
#                 time += 5
#             else:
#                 if i in answer:
#                     answer.remove(i)
#                     answer.append(i)
#                     time += 1
#                 else:
#                     answer.popleft()
#                     answer.append(i)
#                     time += 5
                
#     return time
def solution(cacheSize, cities):
    answer = []
    time = 0
    idx = 0
    if cacheSize == 0:
        return len(cities)*5
    else:
        for i in cities:
            i = i.lower()
            if i in answer:
                answer.remove(i)
                answer.append(i)
                time += 1
            else:
                time += 5
                if idx < cacheSize:
                    idx += 1
                    answer.append(i)
                else:
                    answer.pop(0)
                    answer.append(i)
                
    return time
print(solution(30,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))