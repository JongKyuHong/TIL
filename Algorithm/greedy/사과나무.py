n = int(input())
array=list(map(int,input().split()))
suma = sum(array)
turn = suma//3
if suma % 3 !=0:
    print('NO')
else:
    for a in array:
        turn -=(a//2)
    if turn > 0:
        print('NO')
    else:
        print('YES')

