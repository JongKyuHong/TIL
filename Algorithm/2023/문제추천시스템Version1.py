from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

N = int(input())
MAX_Q = []
MIN_Q = []
visited = defaultdict(bool)
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(MAX_Q, [-L, -P])
    heapq.heappush(MIN_Q, [L, P])
    visited[P] = True
M = int(input())
for _ in range(M):
    inp = input().split()
    if inp[0] == 'add':
        P, L = int(inp[1]), int(inp[2])
        while MAX_Q and not visited[-MAX_Q[0][1]]:
            heapq.heappop(MAX_Q)
        while MIN_Q and not visited[MIN_Q[0][1]]:
            heapq.heappop(MIN_Q)
        heapq.heappush(MAX_Q, [-L, -P])
        heapq.heappush(MIN_Q, [L, P])
        visited[P] = True
    elif inp[0] == 'recommend':
        if inp[1] == '1':
            while not visited[-MAX_Q[0][1]]:
                heapq.heappop(MAX_Q)
            print(-MAX_Q[0][1])
        else:
            while not visited[MIN_Q[0][1]]:
                heapq.heappop(MIN_Q)
            print(MIN_Q[0][1])
    else:
        visited[int(inp[1])] = False