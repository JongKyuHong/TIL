t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = list(map(int,input().split()))
    cnt = 10
    array.sort()
    new_array = []
    while cnt>0:
        if cnt %2 == 0:
            new_array.append(array.pop(-1))
        else:
            new_array.append(array.pop(0))
        cnt -= 1
    print(f'#{test_case}', *new_array)







 