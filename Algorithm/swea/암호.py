for test_case in range(int(input())):
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    index = m
    while k > 0:
        if index > len(numbers):
            index -= len(numbers)
        if index == 0:
            numbers.insert(0,numbers[0] + numbers[-1])
        elif  index == len(numbers):
            numbers.append(numbers[0]+numbers[-1])
        else:
            numbers.insert(index, numbers[index-1] + numbers[index])
        index += m
        k -= 1
    if len(numbers) > 10:
        print(f'#{test_case+1}', *numbers[-10:][::-1])
    else:
        print(f'#{test_case+1}', *numbers[::-1])        




