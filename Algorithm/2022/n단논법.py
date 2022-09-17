import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(26)]

for _ in range(n):
    a, b, c = input().split()
    graph[ord(a)-97].append(c)

m = int(input())
for _ in range(m):
    a, b, c = input().split()
    flag = 0
    q = [a]
    while q:
        now = heapq.heappop(q)
        for next_node in graph[ord(now)-97]:
            if next_node == c:
                flag = 1
                break
            heapq.heappush(q,(next_node))
    if flag:
        print('T')
    else:
        print('F')

    



