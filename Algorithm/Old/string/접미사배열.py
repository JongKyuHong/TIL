n = input()
res = []
for i in range(len(n)):
    res.append(n[i:])
res.sort()
for i in res:
    print(i)