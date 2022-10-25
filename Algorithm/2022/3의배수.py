import sys
input = sys.stdin.readline

X = list(input().rstrip())
convert = 0
if len(X) == 1:
    print(0)
    if int(X[0]) % 3 == 0:
        print('YES')
    else:
        print('NO')
    exit()
while 1:
    sum_v = 0
    for i in X:
        sum_v += int(i)
    convert += 1
    if sum_v < 10:
        print(convert)
        if sum_v in [3,6,9]:
            print('YES')
        else:
            print('NO')
        break
    X = list(str(sum_v))
