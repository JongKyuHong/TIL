import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x: (x[0],x[1]))
    q = []
    for job in jobs:
        heapq.heappush(q, (job[1],job[0]))

    sum_v = 0
    res = []
    while q:
        end, start = heapq.heappop(q)
        if sum_v < start:
            sum_v = end
            res.append(end-start)
        else:
            sum_v += end
            res.append(sum_v-start)
        print(end, start, sum_v, res)
        

    return int(sum(res)/len(res))

#print(solution([[0,3],[1,9],[4,6]]))
print(solution([[7, 8], [3, 5], [9, 6]]))