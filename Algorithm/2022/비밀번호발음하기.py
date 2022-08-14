while 1:
    n = input()
    if n == 'end':
        break
    mo = ['a','e','i','o','u']
    flag,check = 0, 0
    mo_cnt, ja_cnt, before, idx = 0, 0, '', 0
    for i in n:
        if idx == 0:
            before = i
        if i in mo:
            flag = 1
            mo_cnt += 1
            ja_cnt = 0
            if mo_cnt == 3:
                check = 1
                break
        else:
            ja_cnt += 1
            mo_cnt = 0
            if ja_cnt == 3:
                check = 1
                break
        if before == i and idx != 0:
            if i !='e' and i != 'o':
                check = 1
                break
        idx += 1
        before = i

    if check or flag == 0:
        print(f'<{n}> is not acceptable.')
    elif flag and check == 0:
        print(f'<{n}> is acceptable.')
