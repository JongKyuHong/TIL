import sys
input = sys.stdin.readline

n = int(input())
sticks = list(int(input()) for _ in range(n))

target = sticks[-1]
ans = 1
for i in range(len(sticks)-2, -1, -1):
    if target < sticks[i]:
        ans += 1
        target = sticks[i]
print(ans)