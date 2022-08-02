n = int(input())

if n == 2:
    a, b = map(int, input().split())
    res = []
    len_ = a if a < b else b
    for i in range(1, len_+1):
        if a % i == 0 and b % i == 0:
            res.append(i)
    for i in res:
        print(i)
else:
    a, b, c = map(int, input().split())
    len_ = min(a,b,c)
    res = []
    for i in range(1, len_+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            res.append(i)
    for i in res:
        print(i)