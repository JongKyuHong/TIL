import heapq

for _ in range(int(input())):
    k = int(input())
    listN = [input().split() for _ in range(k)]
    Q = []
    Q2 = []
    flag, idx = 0, 0
    visited = [False] * 1000001
    for st, v in listN:
        if st == 'I':
            v = int(v)
            heapq.heappush(Q, (v, idx))
            heapq.heappush(Q2, (-v, idx))
            visited[idx] = True
            idx += 1
        elif st == 'D':
            if v == '1':
                while Q2 and not visited[Q2[0][1]]:
                    heapq.heappop(Q2)
                if Q2:
                    visited[Q2[0][1]] = False
                    heapq.heappop(Q2)
            else:
                while Q and not visited[Q[0][1]]:
                    heapq.heappop(Q)
                if Q:
                    visited[Q[0][1]] = False
                    heapq.heappop(Q)
                

    while Q and not visited[Q[0][1]]:
        heapq.heappop(Q)
    while Q2 and not visited[Q2[0][1]]:
        heapq.heappop(Q2)
    
    if Q and Q2:
        print(-Q2[0][0], Q[0][0])
    else:
        print('EMPTY')
    