def zero(s):
    zero_cnt = 0
    ans = ''
    for i in s:
        if i == '0':
            zero_cnt += 1
        elif i == '1':
            ans += i
    ans_len = len(ans)
    ans = bin(ans_len)
    return [ans[2:], zero_cnt]

def solution(s):
    zero_ans = 0
    change_cnt = 0
    while s != '1':
        change_cnt += 1
        [s,zero_cnt] = zero(s)
        zero_ans += zero_cnt    
    return [change_cnt, zero_ans]