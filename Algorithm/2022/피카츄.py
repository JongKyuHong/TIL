import sys
input = sys.stdin.readline

S = input().rstrip()
idx = 0
flag = 0
while idx < len(S):
    try:
        if S[idx] == 'p':
            if S[idx] + S[idx+1] != 'pi':
                flag = 1
                break
            else:
                idx += 2
        elif S[idx] == 'k':
            if S[idx] + S[idx+1] != 'ka':
                flag = 1
                break
            else:
                idx += 2
        elif S[idx] == 'c':
            if S[idx] + S[idx+1] + S[idx+2] != 'chu':
                flag = 1
                break
            else:
                idx += 3
        else:
            flag = 1
            break
    except:
        flag = 1
        break
if flag:
    print('NO')
else:
    print('YES')