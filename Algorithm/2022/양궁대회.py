def dfs(res, n, idx, info):
    global value, answer
    if n == 0:
        score = 0
        a_score = 0
        for i in range(11):
            if res[i] > info[i]:
                score += 10-i
            elif info[i] != 0 and res[i] <= info[i]:
                a_score += 10-i
        if score-a_score > value:
            value = score-a_score
            answer = res[:]
        elif score-a_score == value:
            for i in range(10, -1, -1):
                if answer[i] < res[i]:
                    answer = res[:]
                    return
                elif answer[i] > res[i]:
                    return
    elif idx == 11:
        if n > 0:
            score = 0
            a_score = 0
            for i in range(11):
                if i == 10:
                    if res[i] + n > info[i]:
                        score += 10-i
                    elif info[i] != 0 and res[i] + n <= info[i]:
                        a_score += 10-i
                else:
                    if res[i] > info[i]:
                        score += 10-i
                    elif info[i] != 0 and res[i] <= info[i]:
                        a_score += 10-i
            
            if score-a_score > value:
                res[10] += n
                value = score-a_score
                answer = res[:]
                res[10] -= n
                return
            elif score-a_score == value:
                for i in range(10, -1, -1):
                    if i == 10:
                        if answer[i] < res[i]+n:
                            res[i] += n
                            answer = res[:]
                            res[i] -= n
                            return
                        elif answer[i] > res[i]+n:
                            return
                    else:
                        if answer[i] < res[i]:
                            answer = res[:]
                            return
                        elif answer[i] > res[i]:
                            return
        return
    else:
        for i in range(idx, 11):
            ######### 하나 더 증가 시키는 경우
            # n이 0보다 작을때 안념겨서 아예 못들어온 상태로 넘어오네 i가 10일때는 무조건 넘기는 코드 사용해야함
            n -= (info[i] + 1)
            if n < 0:
                n += (info[i]+1)
                if i == 10:
                    dfs(res, n, 11, info)
                continue
            res[i] += (info[i]+1)
            dfs(res, n, i+1, info)
            res[i] -= (info[i]+1)
            n += (info[i]+1)
            ######### 같이 상쇄만 시키는 경우
            n -= info[i]
            if n < 0:
                n += info[i]
                if i == 10:
                    dfs(res, n, 11, info)
                continue
            res[i] += info[i]
            dfs(res, n, i+1, info)
            res[i] -= info[i]
            n += info[i]

value = 0
answer = [0]*11
def solution(n, info):
    global answer, value
    result = [0]*11
    for i in range(11):
        n -= (info[i] + 1)
        if n < 0:
            n += (info[i]+1)
            if i == 10:
                dfs(result, n, 11, info)
            continue
        result[i] += (info[i]+1)
        dfs(result, n, i+1, info)
        result[i] -= (info[i]+1)
        n += (info[i]+1)
        ######### 같이 상쇄만 시키는 경우
        n -= info[i]
        if n < 0:
            n += info[i]
            if i == 10:
                dfs(result, n, 11, info)
            continue
        result[i] += info[i]
        dfs(result, n, i+1, info)
        result[i] -= info[i]
        n += info[i]
    return [-1] if value == 0 else answer