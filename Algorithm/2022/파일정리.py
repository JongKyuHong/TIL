N = int(input())

listN = {}

for _ in range(N):
    a, b = input().split(".")
    if b in listN:
        listN[b] += 1
    else:
        listN[b] = 1

d1 = sorted(listN.items())


for k, v in d1:
    print(k, v)