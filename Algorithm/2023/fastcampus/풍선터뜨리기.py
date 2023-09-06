from collections import deque
import sys 
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))
lst = deque([])
for i in range(N):
    lst.append([i+1, tmp[i]])

answer = deque([])
idx = 0
index, current = lst.popleft()
answer.append(index)
for j in range(N-1):
    if current > 0:
        for i in range(current-1):
            x = lst.popleft()
            lst.append(x)
    else:
        for i in range(-current):
            x = lst.pop()
            lst.appendleft(x)
    index, current = lst.popleft()
    answer.append(index)
print(*answer)