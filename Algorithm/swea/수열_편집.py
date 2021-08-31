for test_case in range(int(input())):
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(m):
        array = list(input().split())
        if array[0] == 'I':
            numbers.insert(int(array[1]), int(array[2]))
        elif array[0] == 'D':
            numbers.pop(int(array[1]))
        elif array[0] == 'C':
            numbers[int(array[1])] = int(array[2])
    print(numbers)
    if len(numbers) > l:
        print(f'#{test_case+1} {numbers[l]}')
    else:
        print(f'#{test_case+1} -1')


