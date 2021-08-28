def check(arr):
    bingo_check = 0
    flag = 0
    for i in range(5):
        flag = 0
        for j in range(5):
            if arr[i][j] == 0:
                flag += 1
        if flag == 5:
            bingo_check += 1
    
    if bingo_check >= 3:
        return 1

    flag = 0
    for i in range(5):
        flag = 0
        for j in range(5):
            if arr[j][i] == 0:
                flag += 1
        if flag == 5:
            bingo_check += 1

    if bingo_check >= 3:
        return 1

    flag = 0
    for i in range(5):
        if arr[i][i] == 0:
            flag += 1
    if flag == 5:
        bingo_check += 1

    if bingo_check >= 3:
        return 1

    flag = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            flag += 1
    if flag == 5:
        bingo_check += 1

    if bingo_check >= 3:
        return 1
    else:
        return 0

bingo = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
end_flag = 0
for i in range(5):
    for j in range(5):
        flag2 = 0
        for k in range(5):
            for l in range(5):
                if numbers[i][j] == bingo[k][l]:
                    bingo[k][l] = 0
                    cnt += 1
                    flag2 = 1
                    c = check(bingo)
                    break
            if flag2 == 1:
                break
        if c:
            break
        # if cnt >= 15:
        #    if check(bingo):
        #        end_flag = 1
        #        break
    # if end_flag == 1:
    #     break
    if c:
        break
print(cnt)
