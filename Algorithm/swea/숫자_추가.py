for test_case in range(int(input())):
    n, m, l = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(m):
        index, value = map(int, input().split())
        array.insert(index, value)
    print(f'#{test_case+1} {array[l]}')



