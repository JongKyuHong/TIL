import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]

col = 0
for i in range(N):
    if 'X' not in lst[i]:
        col += 1
row = 0
for i in range(M):
    flag = 0
    for j in range(N):
        if 'X' == lst[j][i]:
            flag = 1
            break
    if not flag:
        row += 1
print(max(row, col))
