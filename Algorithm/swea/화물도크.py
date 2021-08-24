for test_case in range(int(input())):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    array.sort(key = lambda x: x[1])
    prev = array[0][1]
    cnt = 1
    for a,b in array:
        if prev <= a:
            prev = b
            cnt += 1
    print(f'#{test_case+1} {cnt}')




