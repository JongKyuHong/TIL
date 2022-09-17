for T in range(int(input())):
    n, m = map(int, input().split()) # 화물 수, 트럭수
    w = list(map(int, input().split())) # 화물무게
    t = list(map(int, input().split())) # 트럭 적재용량
    res_t = []
    w.sort()
    t.sort()
    idx = 0
    visited = [0]*n
    res = 0
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if t[i] >= w[j] and not visited[j]:
                visited[j] = 1
                res += w[j]
                break
    print(f'#{T+1} {res}')

