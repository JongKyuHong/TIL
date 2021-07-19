def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        comp = ""
        count = 1
        prev = s[:i]
        for j in range(i,len(s),i):
            second = s[j:j+i]
            if prev == second:
                count += 1
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = second
                count = 1
        comp += str(count) + prev if count >= 2 else prev
        answer = min(answer,len(comp))
    return answer

print(solution("aabbaccc"))