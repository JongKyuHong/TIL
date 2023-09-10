import sys 
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    lst = []
    for _ in range(M//10+1):
        lst.extend(list(map(int, input().split())))
    left, right = [], []
    mid = lst[0]
    answer = [lst[0]]
    for i in range(1, len(lst)):
        if mid > lst[i]:
            heapq.heappush(left, -lst[i])
        else:
            heapq.heappush(right, lst[i])
        if i % 2 == 0: 
            if len(left) > len(right):
                while 1:
                    leftvalue = -heapq.heappop(left)
                    heapq.heappush(right, mid)
                    mid = leftvalue
                    if len(left) == len(right):
                        break
            elif len(left) < len(right):
                while 1:
                    rightvalue = heapq.heappop(right)
                    heapq.heappush(left, -mid)
                    mid = rightvalue
                    if len(left) == len(right):
                        break
            answer.append(mid)
    print(len(answer))
    idx = 0
    while idx < len(answer):
        print(answer[idx], end=' ')
        idx += 1
        if idx % 10 == 0:
            print('\n', end='')
    print()