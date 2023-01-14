import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()
q = [lst[0][1]]
for i in range(1, N):
    tmp_end = heapq.heappop(q)
    if tmp_end <= lst[i][0]:
        heapq.heappush(q, lst[i][1])
    else:
        heapq.heappush(q, tmp_end)
        heapq.heappush(q, lst[i][1])

print(len(q))