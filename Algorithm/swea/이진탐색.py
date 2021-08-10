t = int(input())

for test_case in range(1,t+1):
    p,a,b = map(int,input().split())
    check = [a,b]
    result = []
    for i in range(2):
        start = 1
        end = p
        cnt = 0
        while end > start:
            mid = int((end+start)/2)
            cnt += 1
            if mid > check[i]:
                end = mid
            elif mid < check[i]:
                start = mid
            else:
                break
        result.append(cnt)
    if result[0] < result[1]:
        print(f'#{test_case} A')
    elif result[0] > result[1]:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')




