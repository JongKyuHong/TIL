t = int(input())

for test_case in range(1,t+1):
    str1 = input()
    str2 = input()
    maxa = 0
    for i in str1:
        cnt = 0
        for j in range(len(str2)):
            if i == str2[j]:
                cnt += 1
        maxa = max(maxa,cnt)
    print(f'#{test_case} {maxa}')




