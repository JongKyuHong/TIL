def solution(record):
    answer = []
    dic = {}
    for i in record:
        i_s = i.split()
        if len(i_s) == 3:
            dic[i_s[1]] = i_s[2]
    for i in record:
        i_s = i.split()
        if i_s[0] == 'Enter':
            answer.append(f'{dic[i_s[1]]}님이 들어왔습니다.')
        elif i_s[0] == 'Leave':
            answer.append(f'{dic[i_s[1]]}님이 나갔습니다.')
            
            
solution(["Enter uid1234 Muzi", 
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"])
    
    