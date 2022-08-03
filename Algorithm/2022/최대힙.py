n = int(input())
res = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if res:
            print(res.pop(res.index(max(res))))
        else:
            print(0)
    else:
        res.append(x)