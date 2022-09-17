import sys
import heapq
input = sys.stdin.readline


for T in range(int(input())):
    k = int(input())
    visited = [0] * 1000001
    graph = [list(input().rstrip().split()) for _ in range(k)]
    Q_min = []
    Q_max = []
    idx = 0
    for st, v in graph:
        if st == 'I':
            v = int(v)
            heapq.heappush(Q_min, (v, idx))
            heapq.heappush(Q_max, (-v, idx))
            visited[idx] = 1
            idx += 1
        else:
            if v == '1':
                while Q_max and not visited[Q_max[0][1]]:
                    heapq.heappop(Q_max)
                if Q_max:
                    visited[Q_max[0][1]] = 0
                    heapq.heappop(Q_max)
            else:
                while Q_min and not visited[Q_min[0][1]]:
                    heapq.heappop(Q_min)
                if Q_min:
                    visited[Q_min[0][1]] = 0
                    heapq.heappop(Q_min)
    while Q_max and not visited[Q_max[0][1]]:
        heapq.heappop(Q_max)
    while Q_min and not visited[Q_min[0][1]]:
        heapq.heappop(Q_min)
    
    if Q_max and Q_min:
        print(-Q_max[0][0], Q_min[0][0])
    else:
        print('EMPTY')