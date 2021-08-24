def r(a,b):
    if array[a] > array[b]:
        if array[a] == 3 and array[b] == 1:
            return b
        else:
            return a
    elif array[a] < array[b]:
        if array[b] == 3 and array[a] == 1:
            return a
        else:
            return b
    else:
        return a



def check(start,end):
    if start == end:
        return start
    else:
        a = check(start,(start+end)//2)
        b = check(((start+end)//2)+1,end)
        return r(a,b)



for test_case in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    a = check(0,n-1)
    print(f'#{test_case+1} {a+1}')




