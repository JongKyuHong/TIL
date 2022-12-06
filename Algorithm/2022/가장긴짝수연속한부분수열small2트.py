import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

end = 0
odd = 0
res = []
ans = 0
for start in range(n):
    while end < n and odd <= k:
        if lst[end] % 2:
            odd += 1
        else:
            res.append(lst[end])
        end += 1
    ans = max(ans, len(res))

    if lst[start] % 2:
        odd -= 1
    else:
        res.pop(0)
print(ans)
