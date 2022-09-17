while 1:
    n = int(input())
    if n == 0:
        break
    res = []
    for _ in range(n):
        m = input()
        M = m.lower()
        res.append((M,m))
    res = sorted(res, key = lambda x: x[0])
    print(res[0][1])