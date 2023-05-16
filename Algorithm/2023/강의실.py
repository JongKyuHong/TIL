import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    number, start, end = map(int, input().split())
    lst.append((number, start, end))
lst.sort(key=lambda x:x[1])
cnt = 0
tmp = []
for number, start, end in lst:
    if not tmp:
        heapq.heappush(tmp, (end))
    else:
        flag = 0
        for i in range(len(tmp)):
            if tmp[i] <= start:
                tmp[i] = end
                flag = 1
                break
        if not flag:
            heapq.heappush(tmp, (end))

print(len(tmp))