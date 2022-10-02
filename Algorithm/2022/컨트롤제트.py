def solution(s):
    answer = 0
    s = s.split()
    res = []
    for i in s:
        if i == 'Z':
            if res:
                target = res.pop()
                answer -= target
        else:
            i = int(i)
            answer += i
            res.append(i)
            
    return answer

print(solution("10 Z 20 Z 1"))