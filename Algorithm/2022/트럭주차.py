import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
time = [0]*101
for _ in range(3):
    enter, leave = map(int, input().split())
    for i in range(enter, leave):
        time[i] = time[i] + 1
ans = 0
for i in range(101):
    if time[i] == 1:
        ans += a
    elif time[i] == 2:
        ans += (2*b)
    elif time[i] == 3:
        ans += (3*c)
print(ans)