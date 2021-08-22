for test_case in range(1,11):
    len_test = int(input())
    array = map(int,input().split())
    res = 0
    for i in range(2,len(array)-2):
        if array[i] > array[i-2] and  array[i] > array[i-1] and array[i] > array[i+1] and array[i] > array[i+2]:
            cnt = max(array[i-2],array[i-1],array[i+1],array[i+1])
            res += cnt
    print(f'#{test_case} {res}')


