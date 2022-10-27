# import math
# def solution(begin, end):
#     graph = [0]*(end-begin+1)
#     for i in range(begin, end+1):
#         if i % 2:
#             if i == 1:
#                 graph[i-begin] = 0
#             else:
#                 k = 0
#                 for j in range(2, int(math.sqrt(i))+1):
#                     if i % j == 0:
#                         print(j, i, 'asdf')
#                         k = i//j
#                         if k > 10000000:
#                             continue
#                         break
#                 if k == 0:
#                     graph[i-begin] = 1
#                 else:
#                     graph[i-begin] = k
#         else:
#             graph[i-begin] = i//2
    
#     return graph[:end-begin+1]

# import math
# def solution(begin, end):
#     graph = [0]*(end-begin+1)
#     for i in range(begin, end+1):
#         if i % 2:
#             if i == 1:
#                 graph[i-begin] = 0
#             else:
#                 k = 0
#                 for j in range(2, int(math.sqrt(i))+1):
#                     if i % j == 0:
#                         print(j, i, 'asdf')
#                         k = i//j
#                         if k < 10000000:
#                             break
#                 if k == 0 or k >= 10000000:
#                     graph[i-begin] = 1
#                 else:
#                     graph[i-begin] = k
#         else:
#             graph[i-begin] = i//2
    
#     return graph[:end-begin+1]

import math
def solution(begin, end):
    graph = [0]*(end-begin+1)
    for i in range(begin, end+1):
        if i == 1:
            graph[i-begin] = 0
        else:
            k = 0
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    k = i//j
                    if k < 10000000:
                        break
            if k == 0 or k >= 10000000:
                graph[i-begin] = 1
            else:
                graph[i-begin] = k
    
    return graph[:end-begin+1]

#print(solution(1, 10))
#print(solution(1,10000))
#print(solution(999990001,1000000000))
print(solution(999999990,1000000000))