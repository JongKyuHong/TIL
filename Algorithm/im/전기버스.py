for test_case in range(int(input())):
    k, n, m = map(int, input().split())
    array = list(map(int, input().split()))
    if array[-1] != n:
        array.append(n)
    start, cnt, flag, a = 0, 0, 0, 0
    while a < m+1:
        if array[a] - start > k:
            start = array[a-1]
            if array[a] - start <= k:
                cnt += 1
            else:
                cnt = 0
                flag = 1
                break
        elif array[a] - start == k:
            if a == m:
                break
            start = array[a]
            cnt += 1
        a += 1
    print(f'#{test_case+1} {cnt}')



