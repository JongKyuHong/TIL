def solution(polynomial):
    polynomial = polynomial.replace('+','').split()
    cnt = -1
    num_cnt = -1
    for i in polynomial:
        if i[-1] == 'x':
            if len(i) > 1:
                if cnt == -1:
                    cnt = int(i[:-1])
                else:
                    cnt += int(i[:-1])
            else:
                if cnt == -1:
                    cnt = 1
                else:
                    cnt += 1
        else:
            if num_cnt == -1:
                num_cnt = int(i)
            else:
                num_cnt += int(i)
    if num_cnt > -1 and cnt > -1:
        if cnt == 1:
            return 'x + ' + str(num_cnt)
        else:
            return str(cnt)+'x + ' + str(num_cnt)
    elif num_cnt > -1 and cnt == -1:
        return str(num_cnt)
    elif num_cnt == -1 and cnt > -1:
        if cnt == 1:
            return 'x'
        else:
            return str(cnt)+'x'

print(solution("x + 9 + 1"))