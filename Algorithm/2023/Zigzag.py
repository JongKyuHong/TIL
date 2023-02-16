import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
max_l = 2
cnt = 2
for i in range(N-2):
    if lst[i] <= lst[i+1] and lst[i+1] <= lst[i+2]:
        cnt = 2
    elif lst[i] >= lst[i+1] and lst[i+1] >= lst[i+2]:
        cnt = 2
    else:
        cnt += 1
    max_l = max(max_l, cnt)
print(max_l)


