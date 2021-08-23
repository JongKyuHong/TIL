for _ in range(1,11):
    tc = int(input())
    graph = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0
    for i in graph:
        cnt = max(cnt,sum(i))
    for i in range(100):
        cnt1 = 0
        for j in range(100):
            cnt1 += graph[j][i]
        cnt = max(cnt,cnt1)
    cnt2 = 0
    for i in range(100):
        cnt2 += graph[i][i]
    cnt = max(cnt,cnt2)
    cnt3 = 0
    for i in range(100):
        cnt3 += graph[i][99-i]
    cnt = max(cnt,cnt3)

    print(f'#{tc} {cnt}')


