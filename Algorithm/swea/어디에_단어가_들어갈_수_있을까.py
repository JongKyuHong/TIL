t = int(input())

for test_case in range(1,t+1):
    n,k = map(int,input().split())  # 단어퍼즐의 가로세로길이, 단어의길이
    array = [list(map(int,input().split())) for _ in range(n)]
    total = 0
    cnt_list = [0 for _ in range(n+1)]
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == array[i][j]:
                cnt += 1
            else:
                if prev == 1:
                    prev = array[i][j]
                    cnt_list[cnt] += 1
                    cnt = 1
                else:
                    prev = array[i][j]
                    cnt = 1
            if j == n-1:
                if prev == 1:
                    cnt_list[cnt] += 1
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == array[j][i]:
                cnt += 1
            else:
                if prev == 1:
                    prev = array[j][i]
                    if cnt == 3:
                        print(i,'번째')
                    cnt_list[cnt] += 1
                    cnt = 1
                else:
                    prev = array[j][i]
                    cnt = 1
            if j == n-1:
                if prev == 1:
                    cnt_list[cnt] += 1
    print(cnt_list)
    total = cnt_list[k]
    print(f'#{test_case} {total}')


