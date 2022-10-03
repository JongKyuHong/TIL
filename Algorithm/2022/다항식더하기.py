def solution(polynomial):
    polynomial = polynomial.split()
    cnt = -1
    num_cnt = -1
    prev = ''
    for i in polynomial:
        if not prev:
            prev = i
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
        elif i != '+':
            if num_cnt == -1:
                num_cnt = int(i)
            else:
                num_cnt += int(i)
    print(len(prev), prev)
    if num_cnt > -1 and cnt > -1:
        if len(prev) > 1:
            return str(cnt)+ 'x ' + '+ ' + str(num_cnt)
        else:
            return str(num_cnt) + ' + ' + str(cnt) + 'x'
    elif num_cnt > -1 and cnt == -1:
        return str(num_cnt)
    elif num_cnt == -1 and cnt > -1:
        return str(cnt)+'x'

print(solution("11x + 1x + 9"))