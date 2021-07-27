from collections import deque

n = int(input())
array = list(map(int,input().split()))

queue = deque(array)
count = 0
result = 0
while len(queue) >= 2:
    st = queue.popleft()
    en = queue.popleft()
    if st > en:
        count += 1
        queue.appendleft(st)
    else:
        queue.appendleft(en)
        result = max(result,count)
        count = 0

print(result)