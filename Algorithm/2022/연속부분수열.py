def solution(elements):
    answer = 0
    for i in range(1, len(elements)):
        dic = []
        w, c = 0, i
        while 1:
            ans = 0
            if w < c:
                for i in range(w, c):
                    ans += elements[i]
            elif w > c:
                for i in range(c):
                    ans += elements[i]
                for i in range(w, len(elements)):
                    ans += elements[i]
            if ans not in dic:
                dic.append(ans)
            w += 1
            c += 1
            if c == len(elements):
                c = 0
            if w == len(elements):
                break
        answer += len(dic)
    return answer
print(solution([7,9,1,1,4]))