for test_case in range(1,11):
    len_test = int(input())
    array = list(map(int,input().split()))
    res = 0
    for i in range(2,len_test-2):
        cnt = 0
        if array[i] > array[i-2] and  array[i] > array[i-1] and array[i] > array[i+1] and array[i] > array[i+2]:
            cnt = max(array[i-2],array[i-1],array[i+1],array[i+2])
            res += array[i] - cnt
    print(f'#{test_case} {res}')


