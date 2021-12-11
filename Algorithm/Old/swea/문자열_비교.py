t = int(input())

for test_case in range(1,t+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
    

