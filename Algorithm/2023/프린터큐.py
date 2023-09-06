import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    importance = list(map(int, input().split())) # 중요도
    lst = [i for i in range(N)]
    lst.reverse()
    tmp = [] # 큐에서 빠진 인덱스
    while lst:
        idx = lst[-1]
        flag = 0
        for i in range(N):
            if i == idx or i in tmp:
                continue
            if importance[i] > importance[idx]:
                t = lst.pop()
                lst.insert(0, t)
                flag = 1
                break
        if not flag:
            tmp.append(lst.pop())
            if tmp[-1] == M:
                print(len(tmp))
                break
                
                
            

        
