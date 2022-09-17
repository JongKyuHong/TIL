n = int(input())
res = [int(input()) for _ in range(n)]
res.sort()
len_res = len(res)
idx = 0
value = 0
while len_res > 0:
    value = max(value, res[idx]*len_res)
    idx += 1
    len_res -= 1

print(value)