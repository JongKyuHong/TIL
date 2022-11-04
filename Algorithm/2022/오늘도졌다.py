import sys 
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_v = 0
b_v = 0
check = 0
flag = 0

for a, b in zip(A, B):
    a_v += a 
    if not check:
        if a_v > b_v:
            check = 1
    else:
        if b_v > a_v:
            flag = 1
        elif b_v < a_v:
            flag = 0
    b_v += b
    if not check:
        if a_v > b_v:
            check = 1
    else:
        if b_v > a_v:
            flag = 1
        elif b_v < a_v:
            flag = 0
if flag == 1:
    print('Yes')
else:
    print('No')