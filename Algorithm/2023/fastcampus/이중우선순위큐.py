import heapq
import sys 
input = sys.stdin.readline

T = int(input())
INF = float('inf')
for _ in range(T):
    k = int(input())
    maxQ, minQ = [], []
    visited = [0 for _ in range(k)]
    for i in range(k):
        input_ = input().rstrip().split()
        if input_[0] == 'I':
            heapq.heappush(maxQ, [-int(input_[1]), i])
            heapq.heappush(minQ, [int(input_[1]), i])
        else:
            if input_[1] == '1': # 최대값 삭제
                while maxQ:
                    value, idx = heapq.heappop(maxQ)
                    if not visited[idx]:
                        visited[idx] = 1
                        break
            else:
                while minQ:
                    value, idx = heapq.heappop(minQ)
                    if not visited[idx]:
                        visited[idx] = 1
                        break
    if minQ and maxQ:
        answer1 = INF
        while maxQ:
            value, idx = heapq.heappop(maxQ)
            if not visited[idx]:
                answer1 = -value
                break
        answer2 = -INF
        while minQ:
            value, idx = heapq.heappop(minQ)
            if not visited[idx]:
                answer2 = value
                break
        if answer1 != INF and answer2 != INF:
            print(answer1, answer2)
        else:
            print('EMPTY')
    else:
        print("EMPTY")
    
