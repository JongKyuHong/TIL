import sys
input = sys.stdin.readline

n = int(input())

one_time = 0
two_time = 0
flag = 0
for i in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    if team == '1':
        if flag == 0:
            one_time+= 48*60-(60*m+s)
            print(one_time)
        flag += 1
        if flag == 0:
            if two_time > 0:
                two_time=two_time-(48*60-(60*m+s))
                print(two_time)
    else:
        if flag == 0:
            two_time+=48*60-(60*m+s)
            print(two_time)
        flag-=1
        if flag==0: #이걸 넣으면 비겨.
            if one_time>0:
                one_time=one_time-(48*60-(60*m+s))
                print(one_time)