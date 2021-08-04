from collections import deque

n = int(input()) # 선수숫자
array = list(map(int,input().split())) #선수들
array.sort()
que = deque(array)
cnt=0
while len(que) > 1:
    print(len(que))
    a = que.popleft()
    b = que.popleft()
    cnt += abs(b-a)
    if a > b:
        que.append(b)
    else:
        que.append(a)
print(cnt)
