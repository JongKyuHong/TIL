def solution(brown,yellow):
    answer = []
    browny = (brown-4)/2
    if browny % 2 != 0:
        a = (browny//2)+1
        b = browny//2
    else:
        a = browny/2
        b = browny/2
    while 1:
        if yellow ==(a*b):
            answer.append(a+2)
            answer.append(b+2)
            break
        else:
            a+=1
            b-=1
    return answer

print(solution(10,2))