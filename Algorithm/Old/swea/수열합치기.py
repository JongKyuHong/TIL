for test_case in range(int(input())):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(m)]
    base = array[0]
    for i in range(1,m):
        for j in range(len(base)):
            if base[j] > array[i][0]:
                base[j:j] = array[i]
                break
            elif j == len(base)-1:
                base.extend(array[i])
    print(f'#{test_case+1}', *base[-10:][::-1])