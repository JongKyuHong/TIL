t = int(input())

for test_case in range(1,t+1):
    n = int(input())  
    value = list(map(int,input().split()))
    point = value[-1]
    cnt = 0
    for i in range(len(value)-2,-1,-1):
        if point > value[i]:
            cnt += point - value[i]
        else:
            point = value[i]
    print(f'#{test_case} {cnt}')


