for test_case in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    array = sorted(array, key = lambda x: (x[0], x[1]), reverse=True)
    start = array[0][0]
    end = array[0][1]
    cnt = 1
    for i in range(1, n):
        if start >= array[i][1]:
            start = array[i][0]
            end = array[i][1]
            cnt += 1
    print(f'#{test_case+1} {cnt}')

