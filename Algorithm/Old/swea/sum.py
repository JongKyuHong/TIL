t = int(input())

for tc in range(1,t+1):
    t1 = int(input())
    # array = []
    # for _ in range(100):
    #     array.append(list(map(int,input().split())))
    array = [list(map(int,input().split())) for _ in range(100)]
    maxa = 0
    for i in array:
        maxa = max(maxa,sum(i)) # 행의 최대값이 저장된다.
    
    for i in range(100):
        cnt1 = 0
        for j in range(100):
            cnt1 += array[j][i]
        maxa = max(maxa,cnt1)
    cnt = 0
    for i in range(100):
        cnt += array[i][i]
    cnt2 = 0
    for i in range(100):
        cnt2 += array[i][99-i]
    maxa = max(maxa,cnt,cnt2)
    print(f'#{tc} {maxa}')




