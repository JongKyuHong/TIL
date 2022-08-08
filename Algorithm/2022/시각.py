n, k = map(int, input().split())

hour = 0
minute = 0
second = -1
res = 0

def check(time):
    global res
    if len(list(str(time))) == 2:
        if int(list(str(time))[0]) == k or int(list(str(time))[1]) == k:
            res += 1
            return True
    else:
        if time == k:
            res += 1
            return True
    return False


while 1:
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour > n:
                break

    if check(second):
        continue
    if check(minute):
        continue
    if check(hour):
        continue
print(res)