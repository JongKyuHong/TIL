res = float('inf')
res2 = 0
flag = 0 
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        flag = 1
        res = min(res, n)
        res2 += n
if flag:
    print(res2)
    print(res)
else:
    print(-1)