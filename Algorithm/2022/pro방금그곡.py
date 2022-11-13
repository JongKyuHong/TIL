def solution(m, musicinfos):
    answer = []
    music = []
    for i in range(len(musicinfos)):
        start_time, end_time, name, point = musicinfos[i].split(',')
        start_hour = int(start_time[:2])
        start_minute = int(start_time[3:])
        end_hour = int(end_time[:2])
        end_minute = int(end_time[3:])
        
        start_minute += start_hour * 60
        end_minute += end_hour * 60
        target_time = end_minute-start_minute
        
        target = target_time
        res = ''
        for i in range(len(point)):
            if point[i] == '#':
                tt = chr(ord(res[-1])+7)
                res = res[:-1]
                res += tt
            else:
                res += point[i]
        
        tmp = ''
        idx = 0
        
        while target > 0:
            target -= 1
            tmp += res[idx]
            idx += 1
            if idx == len(res):
                idx = 0
        music.append([tmp,name,target_time])
    
    res = ''
    for i in range(len(m)):
        if m[i] == '#':
            tt = chr(ord(res[-1])+7)
            res = res[:-1]
            res += tt
        else:
            res += m[i]
    # 65 66 67 68 69 70 71
    # A  B  C  D  E  F  G  H
    print(res, music,'res')
    answer_idx = 101
    for tmp, name, tt in music:
        idx = 0
        flag = 0
        t_idx = 0
        t_len = len(tmp)
        while t_idx < t_len:
            if tmp[t_idx] == res[idx]:
                t_flag = 0
                for i in range(len(res)):
                    if t_idx+i >= t_len:
                        t_flag = 1
                        break
                    if tmp[t_idx+i] == res[i]:
                        continue
                    else:
                        t_flag = 1
                        break
                t_idx += i-1
                if not t_flag:
                    flag = 1
                    break
            else:
                idx = 0
            t_idx += 1
        if flag:
            answer.append([tt, answer_idx, name])
            answer_idx -= 1
    
    print(answer)
    if answer:
        answer.sort(key=lambda x: x[1], reverse=True)
        answer.sort(key=lambda x: x[0], reverse=True)

    #answer.sort(key=lambda x : (x[0],x[1]), reverse=True)
    return answer[0][2] if answer else '(None)'

#print(solution("DF", ["06:20,06:50,TEST,DDF"]))# -> "TEST"))
#print(solution('ABCDEFG',["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution('CC#BCC#BCC#BCC#B',["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))