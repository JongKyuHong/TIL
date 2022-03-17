def solution(s):
    answer = ''
    keywords = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    res = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            res += i
            if res in keywords.keys():
                answer += str(keywords[res])
                res =''
    return int(answer)