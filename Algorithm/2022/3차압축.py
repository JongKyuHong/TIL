def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1
    rear = 27
    idx = 0
    while msg:
        print(msg[idx], msg)
        for i in range(1, len(msg)):
            if msg[idx:idx+i] in dic:
                continue
            else:
                tt = msg[idx:idx+i-1]
                answer.append(tt)
                tt = msg[idx:idx+i]
                dic[tt] = rear
                rear += 1
                msg = msg[idx+i:]
                break

    return answer

print(solution('KAKAO'))