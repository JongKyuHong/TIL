from collections import deque
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))
array.reverse()
queue = deque(array)
cnt = 0
while len(queue) >= 2:
    a = queue.popleft()
    b = queue.popleft()
    if a < b:
        cnt += b - a + 1
        queue.appendleft(a-1)
    elif a == b:
        queue.appendleft(a-1)
        cnt += 1
    else:
        queue.appendleft(b)
print(cnt)