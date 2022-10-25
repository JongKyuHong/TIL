def solution(files):
    answer = []
    HEAD = []
    
    for file in files:
        head = ''
        num = ''
        tail = ''
        flag = 0
        for i in file:
            if i.isdigit() and flag < 2:
                flag = 1
                num += i
            elif flag >= 1:
                flag = 2
                tail += i
            else:
                head += i
        HEAD.append([head, num, tail])
    HEAD.sort(key=lambda x: (x[0].lower(),int(x[1])))
    
    for i in HEAD:
        answer.append(''.join(i))
    return answer

print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))
