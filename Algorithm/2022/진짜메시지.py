import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    dic = {}
    i, flag = 0, 0
    while i < len(data):
        if data[i] in dic:
            dic[data[i]] += 1
            if dic[data[i]] == 3:
                if i != len(data)-1:
                    if data[i+1] == data[i]:
                        dic[data[i]] = 0
                        i += 1
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        else:
            dic[data[i]] = 1
        i += 1

    if flag:
        print('FAKE')
    else:
        print('OK')