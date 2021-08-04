from collections import deque
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
que = deque(array)
i = 1
suma = 0
while que:
    suma += abs(i-que.popleft())
    i += 1
print(suma)

