n = int(input())
pos = 1
res = 0

while 1:
    res += pos
    if res > n:
        print(pos-1)
        break
    elif res == n:
        print(pos)
        break
    pos += 1