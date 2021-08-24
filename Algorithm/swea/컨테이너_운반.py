for test_case in range(int(input())):
    n, m = map(int,input().split())  # 컨테이너 수 n, 트럭 수 m
    weight = list(map(int,input().split()))  # 각 화물의 무게
    capacity = list(map(int,input().split()))  # 트럭의 적재 용량
    weight.sort(reverse=True)
    capacity.sort(reverse=True)
    print(weight, 'weight')
    print(capacity,'capa')
    res = 0
    j = 0
    i = 0
    print(n, m)
    while j < n and i < m:
        if weight[j] <= capacity[i]:
            res += weight[j]
            j += 1
            i += 1
        else:
            j += 1

    print(f'#{test_case+1} {res}')