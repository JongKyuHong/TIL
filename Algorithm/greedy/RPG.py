n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

array.sort(key=lambda x:(x[0],x[1]))
ch1,ch2 = 1,1

if ch1 >= array[0][0] or ch2 >= array[0][1]:
    a,b,c = array.pop(0)
    count = n-1
    cnt = 0
    while count > 0 and array:
        a1,b1,c1 = array.pop(0)
        if ch1+c >= a1:
            ch1 += c
            cnt += 1
            c += c1
        elif ch2+c >= b1:
            ch2 += c
            cnt += 1
            c += c1
        else:
            array.append([a1,b1,c1])
        count -= 1
    print(cnt)
else:
    print(-1)
