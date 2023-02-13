import sys
input = sys.stdin.readline

while 1:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for i in range(N, M+1):
            dict = {}
            flag = 0
            for j in str(i):
                if j not in dict:
                    dict[j] = 1
                else:
                    flag = 1
                    break
            if not flag:
                cnt += 1
        print(cnt)
    except: 
        break
