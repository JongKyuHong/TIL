from collections import deque

n, m = map(int, input().split())  # n : 큐의 크기, m : 뽑아내려고 하는 수의 개수
value = list(map(int, input().split()))

q = deque([i+1 for i in range(n)])
count = 0

for x in value:
    while 1:
        if q.index(x) == 0:
            q.popleft()
            break
        if q.index(x) - 0 <= len(q) - q.index(x):
            q.append(q.popleft())
            count += 1
        else:
            q.appendleft(q.pop())
            count += 1
print(count)        
        



