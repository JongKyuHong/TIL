t = int(input())

for test_case in range(1,t+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(n)] # 완벽하게 맞아떨어지고 흰색인곳에 단어가 들어감
    cnt_list = [0 for _ in range(n+1)]
    for i in range(n):
        prev = 2
        cnt = 1
        
        for j in range(n):
            if prev == puzzle[i][j]:
                cnt += 1
            else:
                if prev == 1:
                    prev = puzzle[i][j]
                    cnt_list[cnt] += 1
                    cnt = 1
                else:
                    prev = puzzle[i][j]
                    cnt = 1
            if j == n-1:
                if prev == 1:
                    cnt_list[cnt] += 1
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == puzzle[j][i]:
                cnt += 1
            else:
                if prev == 1:
                    prev = puzzle[j][i]
                    cnt_list[cnt] += 1
                    cnt = 1
                else:
                    prev = puzzle[i][j]
                    cnt = 1
            if j == n-1:
                if prev == 1:
                    cnt_list[cnt] += 1
    total = cnt_list[k]        
    print(f'#{test_case} {total}')






