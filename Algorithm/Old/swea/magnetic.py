for test_case in range(10):
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(n)]
    table = list(zip(*table))
    cnt = 0
    for i in range(n):
        prev, flag = 0, 0
        for j in range(n):
            if table[i][j] != 0 and prev == 0:
                prev = table[i][j]
                flag = 1
            if flag == 1:
                if table[i][j] == 2:
                    if prev != table[i][j]:
                        cnt += 1
                        prev = table[i][j]
                elif table[i][j] == 1:
                    if prev != table[i][j]:
                        prev = table[i][j] 
    print(f'#{test_case+1} {cnt}')