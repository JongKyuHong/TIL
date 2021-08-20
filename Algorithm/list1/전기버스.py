t = int(input())

for test_case in range(1,t+1):
    k, n, m = map(int,input().split())
    bus_stops = list(map(int,input().split()))
    rmn = k
    point = 0
    for i in range(len(bus_stops)):
        if i == len(bus_stops)-1: # 마지막 위치
            if n-point > rmn:  # 마지막 위치까지 안닿으면 1추가
                cnt += 1
        elif bus_stops[i]-point <= rmn:  # 현재위치 - 전위치 
            if bus_stops[i+1] - point > rmn: # 다음위치를 한번에 못간다면 cnt늘리고 kmn도 초기화
                rmn = k
                cnt += 1
            else:  # 다음위치도 한번에 간다면
                rmn -= (bus_stops[i]-point)  # rmn에서 현재위치 - 이전위치 값을빼준다 즉, 앞으로 전진할수있는 값
            point = bus_stops[i]
        else:
            cnt = 0
            break
    
    print(f'#{test_case} {cnt}')
