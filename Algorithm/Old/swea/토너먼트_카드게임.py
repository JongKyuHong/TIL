t = int(input())

def r(start,end):
    if array[start] > array[end]:
        if array[start] == 3 and array[end] == 1:
            return end
        else:
            return start
    elif array[start] < array[end]:
        if array[end] == 3 and array[start] == 1:
            return start
        else:
            return end
    else:
        return start
def check(start,end):
    #하나일때 걸러내는 수가 있어야함
    if start == end:
        return start
    else:
        a = check(start,(start+end)//2)
        b = check(((start+end)//2)+1,end)
        return r(a,b)

for test_case in range(1,t+1):
    n = int(input())
    array = list(map(int,input().split()))
    stack = []
    for idx,val in enumerate(array):
        stack.append([idx,val])
    ans = check(0,n-1)+1
    print(f'#{test_case} {ans}')
    




