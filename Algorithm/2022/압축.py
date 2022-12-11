def solution(msg):
    answer = []
    alpha = []
    for i in range(26):
        alpha.append(chr(65+i))
        
    idx = 0
    while idx < len(msg):
        for i in range(1, len(msg)-idx+1):
            if msg[idx:idx+i] in alpha:
                if idx+i == len(msg):
                    answer.append(alpha.index(msg[idx:idx+i])+1)
                    idx += 1
                    break
                continue
            else:
                alpha.append(msg[idx:idx+i])
                answer.append(alpha.index(msg[idx:idx+i-1])+1)
                idx = idx+i-1
                break
        #print(idx)
    return answer

print(solution('KAKAO'))