def solution(plans):
    answer = []
    # plans 시작시간으로 정렬
    plans.sort(key=lambda x: x[1], reverse=True)
    
    # 잠시 멈춘 과제를 넣을 공간을 만듬
    problem = []
    
    # 시작시간이 짧은 순 으로 시작하고, 대기 스택에 넣을때 남은 시간과 함께 넣음
    now_time = plans[-1][1]
    flag = 0
    while plans:
        print(plans,'plans')
        print(problem,'problem')
        print(answer,'answer')
        print(now_time,'now_time')
        if flag and problem:
            name, playtime = problem.pop()
            start = now_time
            flag = 0
        else:
            name, start, playtime = plans.pop()
            if start > now_time:
                now_time = start
        print(plans,'asdfplans')
        if not plans:
            answer.append(name)
            break
        hour, minute = int(start[0:2]), int(start[3:])
        name2, start2, playtime2 = plans[-1]
        hour2, minute2 = int(start2[0:2]), int(start2[3:])
        print(hour, minute, hour2, minute2)
        hour3 = hour2 - hour
        minute3 = minute2 - minute
        if minute3 < 0:
            minute3 = 60 + minute3
            hour3 -= 1
        time = hour3*60 + minute3
        print(time, playtime)
        if int(playtime) <= time:
            print(now_time, name, name2, time, playtime)
            now_hour, now_minute = int(now_time[:2]), int(now_time[3:])
            now_minute += int(playtime)
            now_hour += now_minute//60
            now_minute %= 60
            now_hour, now_minute = str(now_hour), str(now_minute)
            if len(now_hour) != 2:
                now_hour = '0'+now_hour
            if len(now_minute) != 2:
                now_minute = '0'+now_minute
            now_time = now_hour + ':' + now_minute
            if now_time < start2:
                flag = 1
            if time == int(playtime):
                flag = 0
            print(flag, now_time, start2)
            answer.append(name)
        else:
            now_hour, now_minute = int(now_time[:2]), int(now_time[3:])
            now_minute += time
            now_hour += now_minute//60
            now_minute %= 60
            now_hour, now_minute = str(now_hour), str(now_minute)
            if len(now_hour) != 2:
                now_hour = '0'+now_hour
            if len(now_minute) != 2:
                now_minute = '0'+now_minute
            now_time = now_hour + ':' + now_minute
            problem.append([name, int(playtime)-time])
    
    while problem:
        name,playtime = problem.pop()
        answer.append(name)
    return answer

print(solution([["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]))
#print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
#print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
#print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))