def solution(s):
    answer = 10001
    if len(s) == 1:
        return 1
    else:
        for i in range(1, len(s)//2+1):
            tmp = s[:i]
            res = ''
            cnt = 1
            for n in range(i,len(s)+i,i):
                if tmp == s[n:i+n]:
                    cnt += 1
                else:
                    if cnt == 1:
                        res += tmp
                    else:
                        res += str(cnt) + tmp
                    cnt = 1
                    tmp = s[n:i+n]
            answer = min(len(res),answer)
        return answer
print(solution('a'))