from collections import deque
a, b = map(int,input().split())
count = 0
queue = deque([(a,1)])

while queue:
    i, cnt = queue.popleft()
    if i == b:
        count = cnt
        break
    if i*2 <= b:
        queue.append((i*2,cnt+1))
    if int(str(i)+'1') <=b:
        queue.append((int(str(i)+'1'),cnt+1))
print(count)

        





