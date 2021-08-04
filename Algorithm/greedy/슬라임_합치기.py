from collections import deque
n = int(input())
array = list(map(int,input().split()))
array.sort(reverse=True)
que = deque(array)
result = 0
while len(que)>=2:
    a = que.popleft()
    b = que.popleft()
    st = a + b
    sc = a * b
    que.appendleft(st)
    result += sc
print(result)
