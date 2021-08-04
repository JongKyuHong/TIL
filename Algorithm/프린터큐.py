from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    que = deque(array)
    idx = m
    cnt = 0
    while que:
        maxq = max(que)
        quepop = que.popleft()
        if not que:
            cnt += 1
            break
        if maxq > quepop:
            print(maxq ,"맥스큐")
            print(que , "큐상황")
            que.append(quepop)     
            if idx == 0:
                idx = len(que)
        else:
            print(maxq,"맥스큐2")
            print(que , "큐상황2")
            cnt += 1
            if idx == 0:
                break
        idx -= 1
    print(cnt)         
    
