import sys
input = sys.stdin.readline

h, w = map(int, input().split())
lst = list(map(int, input().split()))

prev = lst[0]
ans = 0
for i in range(1, w-1):
    left_max = max(lst[:i])
    right_max = max(lst[i+1:])

    compare = min(left_max, right_max)
    if lst[i] < compare:
        ans += compare - lst[i]
print(ans)