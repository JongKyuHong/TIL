import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    day = 1
    while 1:
        tmp = N
        for i in range(6):
            tmp -= lst[i]
        if tmp < 0:
            break
        new_lst = []
        for i in range(6):
            if i < 3:
                if i == 0:
                    new_lst.append(lst[i] + lst[5] + lst[i+1] + lst[i+3])
                else:
                    new_lst.append(lst[i] + lst[i-1] + lst[i+1] + lst[i+3])
            else:
                if i == 5:
                    new_lst.append(lst[i] + lst[0] + lst[i-1] + lst[i-3])
                else: 
                    new_lst.append(lst[i] + lst[i-1] + lst[i+1] + lst[i-3])
        day += 1
        lst = new_lst[:]
    print(day)