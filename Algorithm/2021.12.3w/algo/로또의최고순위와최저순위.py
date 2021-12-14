def solution(lottos, win_nums):
    res = 0
    answer = []
    for i in win_nums:
        if i in lottos:
            res += 1
    res2 = res
    res += lottos.count(0)
    if res > 1:            
        answer.append(7-res)
    else:
        answer.append(6)
    if res2 > 1:
        answer.append(7-res2)
    else:
        answer.append(6)
    return answer