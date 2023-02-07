import sys
input = sys.stdin.readline

N = int(input())
days = [0]*366
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        days[i] += 1

row, col = 0, 0
ans = 0
for i in range(366):
    if days[i] != 0:
        row = max(row, days[i])
        col += 1
    else:
        ans += row*col
        row, col = 0, 0

ans += row*col
print(ans)
