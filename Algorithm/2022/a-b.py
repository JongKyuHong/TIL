a,b = map(int, input().split())
flag = 0
cnt = 0
while a != b:
    if b % 2 and str(b)[-1] == '1':
        try:
            b = int(str(b)[:-1])
        except:
            flag = 1
            break
    else:
        b //= 2
    cnt += 1

if flag:
    print(-1)
else:
    print(cnt+1)