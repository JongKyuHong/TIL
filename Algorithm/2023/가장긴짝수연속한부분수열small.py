import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

end = 0
odd = 0
res = []
max_v = 0
for start in range(N):
    while odd <= K and end < N:
        if lst[end] % 2:
            odd += 1
        else:
            res.append(lst[end])
        end += 1
    if max_v < len(res):
        max_v = len(res)
    if lst[start] % 2:
        odd -= 1
    else:
        res.pop(0)
print(max_v)



