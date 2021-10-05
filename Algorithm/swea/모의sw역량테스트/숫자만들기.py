def dfs(idx, result):
    global max_value
    global min_value

    if idx == n-1:
        if result >= max_value:
            max_value = result
        if result <= min_value:
            min_value = result
        return
    
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                new_result = result + numbers[idx+1]
            elif i == 1:
                new_result = result - numbers[idx+1]
            elif i == 2:
                new_result = result * numbers[idx+1]
            else: 
                new_result = int(result / numbers[idx+1])
            dfs(idx+1, new_result)
            operator[i] += 1


for test_case in range(int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    min_value = 99999999
    max_value = -9999990
    numbers = list(map(int, input().split()))
    dfs(0,numbers[0])
    print(f'#{test_case+1} {max_value-min_value}')