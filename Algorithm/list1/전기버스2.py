t = int(input())

for test_case in range(1,t+1):
    k, n, m = map(int,input().split())  # k:최대한 이동할수있는 정류장, n:종점번호, m:충전기설치된곳 개수
    bus_stops = list(map(int,input().split()))
    prev = 0
    cnt = 0
    ch = k
    for i in range(m):
        if i == m-1:
            if n-prev > ch:
                cnt += 1
        elif bus_stops[i]-prev <= ch:
            if bus_stops[i+1] - prev > ch:
                ch = k
                cnt += 1
            else:
                ch -= (bus_stops[i]-prev)
            prev = bus_stops[i]
        else:
            cnt = 0
            print(i, 'hi')
            break

    print(f'#{test_case} {cnt}')








