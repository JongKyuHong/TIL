def r(i, j):
    if array[i] > array[j]:
        if array[i] == 3 and array[j] == 1:
            return j
        else:
            return i
    elif array[i] < array[j]:
        if array[j] == 3 and array[i] == 1:
            return i
        else:
            return j
    else:
        return i


def check(i, j):
    if i == j:
        return i
    else:
        a = check(i,(i+j)//2)
        b = check(((i+j)//2)+1,j)
        return r(a,b)
for test_case in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    res = check(0,n-1)+1
    print(f'#{test_case+1} {res}')



