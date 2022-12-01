import heapq

def solution(n, paths, gates, summits):
    answer = []
    all_path = [[]*(n+1) for _ in range(n+1)]
    max_value = 0
    for path in paths:
        point1, point2, time = path
        all_path[point1].append((point2, time))
        all_path[point2].append((point1, time))
        max_value = max(max_value, time)
    intensity = 0
    
    def dijkstra(start, end, limit):
        q = [[0, start]]
        cost = [float('inf')]*(n+1)
        cost[start] = 0
        max_v = 0
        while q:
            now_cost, now = heapq.heappop(q)
            if cost[now] < now_cost:
                continue
            
            for point, time in all_path[now]:
                sum_cost = now_cost + time
                if time > limit or (point in summits and point != end):
                    continue
                if cost[point] > sum_cost:
                    max_v = max(max_v, time)
                    cost[point] = sum_cost
                    heapq.heappush(q,(sum_cost, point))
        #print(cost,limit,start,end, 'cost')
        return cost[end] != float('inf')

    
    #for gate in gates:
        for summit in summits:
            left = 0
            right = max_value
            while left <= right:
                mid = (left+right)//2
                if dijkstra(gate, summit, mid):
                    #print(gate,summit,mid,'gate summit mid')
                    answer.append([summit, mid])
                    right = mid-1
                else:
                    left = mid+1
    #print(answer)
    answer.sort(key=lambda x:x[1])
    return answer[0]

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]))