n = int(input())

gijun = n // 5
idx = 0
res = 100001
flag = 0
while idx <= gijun:
    coin = 5*idx
    if (n - coin) % 2 == 0:
        flag = 1
        res = min(res, idx + (n-coin)//2)
    idx += 1
if flag:
    print(res)
else:
    print(-1)