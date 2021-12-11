t = int(input())

for test_case in range(1,t+1):
    array = input()
    prev = array[0]
    new_array = []
    for i in range(1,len(array)):
        if prev == '(' and array[i] == ')':
            new_array.append('-')
        
    res = 0
    cnt = 0
    for i in array:
        if i == '-':
            res += cnt
        elif i == '(':
            cnt += 1
        elif i == ')':
            res += 1
            cnt -= 1
    print(f'#{test_case} {res}')



