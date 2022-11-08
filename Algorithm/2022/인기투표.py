import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = [0]*n
    sum_v = 0
    for i in range(n):
        A[i] = int(input())
        sum_v += A[i]
    
    max_v = max(A)
    
    cnt = 0
    for i in range(n):
        if A[i] == max_v:
            cnt += 1
    if cnt > 1:
        print('no winner')
    elif sum_v / 2 < max_v:
        print('majority winner ' + str(A.index(max_v)+1))
    elif sum_v / 2 >= max_v:
        print('minority winner ' + str(A.index(max_v)+1))