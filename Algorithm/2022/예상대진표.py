def solution(n,a,b):
    answer = 0
    if a > b:
        a, b = b, a
    while 1:
        if a > 1:
            n1, q1 = divmod(a, 2)
            if q1 == 0:
                a = (n1-1)*2
            else:
                a = n1*2
            print(a, n1, q1)
        n2, q2 = divmod(b, 2)
        if q2 == 0:
            b = n2-1
        else:
            b = n2
        answer += 1
        #print(a, n1, q1, b)
        if n1 == n2+1 and q1 == 1 and q2 == 0:
            return answer
            
    return answer

print(solution(8,4,7))