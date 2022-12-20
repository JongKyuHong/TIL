import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
lst = [0]*N

idx = 0
lst[idx] = 1
cnt = 0
while 1:
    if lst[idx] == M:
        break
    if lst[idx] % 2:
        idx += L
        idx %= N
    else:
        idx -= L
        idx %= N
    cnt += 1
    lst[idx] += 1
print(cnt)