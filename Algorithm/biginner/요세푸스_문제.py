from collections import deque

n,k = map(int,input().split())

a = list(range(1,n+1))
a = deque(a)
result = []
while a:
    for i in range(k):
        a1 = a.popleft()
        if i != k-1:
            a.append(a1)
        else:
            result.append(a1)

for i in range(n):
    if i == 0:
        print("<",end="")
        print(result[i],end=", ")
    elif i == n-1:
        print(result[i],end=">")
    else:
        print(result[i],end=", ")