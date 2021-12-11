n = int(input())
res = 1
while n != 0:
    res *= n
    n -= 1
res = str(res)
i = -1
cnt = 0
while 1:
    if res[i] == '0':
        cnt += 1
    else:
        break
    i -= 1
print(cnt)




