import sys
input = sys.stdin.readline

while 1:
    try:
        s, t = input().split()
        idx, flag = 0, 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    flag = 1
                    break
        if flag == 1:
            print('Yes')
        else:
            print('No')
    except:
        break
