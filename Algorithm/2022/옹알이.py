def solution(babbling):
    answer = 0
    text = ['aya','ye','woo','ma']
    for bab in babbling:
        prev = ''
        flag1 = 0
        while bab:
            flag = 0
            for i in range(4):
                if i == 0 or i == 2:
                    if text[i] == bab[:3] and prev != bab[:3]:
                        prev = bab[:3] 
                        bab = bab[3:]
                        flag = 1
                        break
                else:
                    if text[i] == bab[:2] and prev != bab[:2]:
                        prev = bab[:2]
                        bab = bab[2:]
                        flag = 1
                        break
            if flag == 0:
                flag1 = 1
                break
        if flag1 == 0:
            answer += 1
    return answer

print(solution(["ayayewoomawooma"]))
print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))