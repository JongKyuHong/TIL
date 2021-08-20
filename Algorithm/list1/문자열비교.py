t = int(input())

for test_case in range(1,t+1):
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        if str2[i] == str1[0]:
            flag = 1
            for j in range(len(str1)):
                if str2[i+j] != str1[j]:
                    flag = 0
                    break
            if flag == 1:
                print(f'#{test_case} 1')
                break
    if flag == 0:
        print(f'#{test_case} 0')
    