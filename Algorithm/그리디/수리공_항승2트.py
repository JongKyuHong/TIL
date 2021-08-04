from collections import deque

n,l = list(map(int,input().split()))

array = list(map(int,input().split()))
array.sort()
que = deque(array)

result = []
count = 0
while que:
    q1 = que.popleft()
    result.append(q1)
    
    for i in range(n):
        if que:
            q2 = que.popleft()
            if (q1+l-1) < q2:
                que.appendleft(q2)
                break
            else:
                result.append(q2)
        else:
            break
    count += 1
    result = []
print(count)