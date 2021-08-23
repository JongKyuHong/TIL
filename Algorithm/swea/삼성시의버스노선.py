t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    bus_route = [list(map(int,input().split())) for _ in range(n)]
    p = int(input())
    bus_stops = [int(input()) for _ in range(p)]
    res = []
    for bus in bus_stops:
        cnt = 0
        for a,b in bus_route:
            if a <= bus <= b:
                cnt += 1
        res.append(cnt)
    print(f'#{test_case}',end=' ')
    for i in res:
        print(i,end=' ')
    print()
    