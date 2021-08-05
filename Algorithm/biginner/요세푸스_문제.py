from collections import deque

n,k = map(int,input().split())

a = list(range(1,n+1))
a = deque(a)
result = []
while a:
    for i in range(k):
        a1 = a.popleft()
        if i == k-1:
            result.append(a1)
        else:
            a.append(a1)

print(f"<{', '.join(map(str,result))}>")