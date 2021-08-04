from collections import deque

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()
queue = deque(rope)
target =  queue.popleft() * n
maxa = target
while n > 1:
    n -= 1
    target = queue.popleft() * n
    if target > maxa:
        maxa = target
print(maxa)