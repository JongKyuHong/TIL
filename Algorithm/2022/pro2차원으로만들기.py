def solution(num_list, n):
    answer = [[]]
    cnt = 0
    tmp = []
    for i in num_list:
        cnt += 1
        tmp.append(i)
        if cnt == n:
            answer.append(tmp)
            tmp = []
            cnt = 0
    
    return answer[1:]