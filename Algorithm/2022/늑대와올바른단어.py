import sys
input = sys.stdin.readline

word = input().rstrip()
idx = 0
flag = 0
while idx < len(word):
    if word[idx] == 'w':
        consi = 1
        while idx+consi < len(word):
            if word[idx+consi] == 'w':
                consi += 1
            else:
                break
        if idx+consi < len(word) and word[idx+consi] == 'o':
            o_consi = 1
            idx += consi
            while idx+o_consi < len(word):
                if word[idx+o_consi] == 'o':
                    o_consi += 1
                else:
                    break
            if idx+o_consi < len(word) and o_consi == consi:
                if word[idx+o_consi] == 'l':
                    l_consi = 1
                    idx += o_consi
                    while idx+l_consi < len(word):
                        if word[idx+l_consi] == 'l':
                            l_consi += 1
                        else:
                            break
                    if idx+l_consi < len(word) and l_consi == consi:
                        if word[idx+l_consi] == 'f':
                            f_consi = 1
                            idx += l_consi
                            while idx+f_consi<len(word):
                                if word[idx+f_consi] == 'f':
                                    f_consi += 1
                                else:
                                    break
                            if f_consi == consi:
                                idx += f_consi
                            else:
                                flag = 1
                                break
                    else:
                        flag = 1
                        break
            else:
                flag = 1
                break
        else:
            flag = 1
            break
    else:
        flag = 1
        break
if flag:
    print(0)
else:
    print(1)
        