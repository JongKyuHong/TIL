import sys
input = sys.stdin.readline

n = int(input())
lst = [1]*(n-1)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x-1, y-1):
        lst[i] = 0
ans = 0
for i in lst:
    if i == 1:
        ans += 1
print(ans+1)
        