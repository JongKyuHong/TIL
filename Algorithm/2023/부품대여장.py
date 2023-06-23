import sys
from collections import defaultdict
input = sys.stdin.readline

def cal(date, time):
    month, day = date[5:7], date[8:10]
    hour, minute = time[:2], time[3:5]
    tmp = (int(day)-1)*24*60 + int(hour)*60 + int(minute)
    month = int(month) - 1
    while month > 0:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            tmp += 31*24*60
        else:
            if month == 2:
                tmp += 28*24*60
            else:
                tmp += 30*24*60
        month -= 1
    return tmp

dic = {}
F_dic = {}
N, L, F = input().rstrip().split()
L_day, L_hour, L_minute = L[:3], L[4:6], L[7:9]
standard = int(L_day)*24*60 + int(L_hour)*60 + int(L_minute)
for i in range(int(N)):
    date, time, name, nickname = input().rstrip().split()
    tmp = cal(date, time)
    if name+nickname not in dic:
        dic[name+nickname] = tmp
    else:
        start_minute = dic[name+nickname]
        if tmp - start_minute > standard:
            if nickname not in F_dic:
                F_dic[nickname] = (tmp - start_minute - standard) * int(F)
            else:
                F_dic[nickname] += (tmp - start_minute - standard) * int(F)
        del dic[name+nickname]
if F_dic:
    for name, f in sorted(F_dic.items(), key=lambda x:x[0]):
        print(name, f)
else:
    print(-1)