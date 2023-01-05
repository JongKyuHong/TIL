import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    MAX_Q = []
    MIN_Q = []
    idx = 0
    visited = [0]*k
    for _ in range(k):
        inp = input().split()
        inp[1] = int(inp[1])
        if inp[0] == 'I':
            heapq.heappush(MAX_Q, [-inp[1],idx])
            heapq.heappush(MIN_Q, [inp[1],idx])
            visited[idx] = 1
            idx +=1
        else:
            if MAX_Q and MIN_Q:
                if inp[1] == 1: # 최댓값 삭제
                    while MAX_Q and not visited[MAX_Q[0][1]]:
                        v, i = heapq.heappop(MAX_Q)
                    if MAX_Q:
                        v, i = heapq.heappop(MAX_Q)
                        visited[i] = 0
                else:   
                    while MIN_Q and not visited[MIN_Q[0][1]]:
                        v, i = heapq.heappop(MIN_Q)
                    if MIN_Q:
                        v, i = heapq.heappop(MIN_Q)
                        visited[i] = 0
                    
    while MAX_Q and not visited[MAX_Q[0][1]]:
        v, i = heapq.heappop(MAX_Q)
    while MIN_Q and not visited[MIN_Q[0][1]]:
        v, i = heapq.heappop(MIN_Q)
    if MAX_Q and MIN_Q:
        print(-MAX_Q[0][0], MIN_Q[0][0])
    else:
        print('EMPTY')