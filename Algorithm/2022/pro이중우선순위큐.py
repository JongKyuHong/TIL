import heapq

def solution(operations):
    q_min = []
    q_max = []
    idx = 0
    visited = [0] * 1000001
    for i in operations:
        a, b = i.split()
        if a == 'I':
            b = int(b)
            heapq.heappush(q_min, (b, idx))
            heapq.heappush(q_max, (-b, idx))
            visited[idx] = 1
            idx += 1
        else:
            if b == '1':
                while q_max and not visited[q_max[0][1]]:
                    heapq.heappop(q_max)
                if q_max:
                    visited[q_max[0][1]] = 0
                    heapq.heappop(q_max)
            else:
                while q_min and not visited[q_min[0][1]]:
                    heapq.heappop(q_min)
                if q_min:
                    visited[q_min[0][1]] = 0
                    heapq.heappop(q_min)
    while q_max and not visited[q_max[0][1]]:
        heapq.heappop(q_max)
    while q_min and not visited[q_min[0][1]]:
        heapq.heappop(q_min)
    if q_max and q_min:
        return [-q_max[0][0], q_min[0][0]]
    else:
        return [0, 0]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])