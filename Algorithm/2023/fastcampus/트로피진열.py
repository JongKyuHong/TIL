import sys 
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

tmp = 0
left_cnt, right_cnt = 0, 0
for i in range(N):
    if tmp == 0:
        tmp = lst[i]
        left_cnt += 1
    else:
        if tmp < lst[i]:
            tmp = lst[i]
            left_cnt += 1

tmp = 0
for i in range(N-1, -1, -1):
    if tmp == 0:
        tmp = lst[i]
        right_cnt += 1
    else:
        if tmp < lst[i]:
            tmp = lst[i]
            right_cnt += 1
print(left_cnt)
print(right_cnt)