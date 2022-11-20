import sys
input = sys.stdin.readline

s, n = map(int, input().split())
lst = [[]*(s+2) for _ in range(2*s+3)]
idx = 0

for a in str(n):
    idx += 1
    if a == '1':
        for j in range(s+2):
            if j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    lst[i] += ' '
    elif a == '2':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i > s+1 and i != 2*s+2:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            elif j == s+1:
                for i in range(2*s+3):
                    if i < s+1 and i != 0:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i==2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '3':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    lst[i] += ' '
            elif j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i==2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '4':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i < s+1 and i != 0:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            elif j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    if i == s+1:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '5':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i < s+1 and i != 0:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            elif j == s+1:
                for i in range(2*s+3):
                    if i > s+1 and i != 2*s+2:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '6':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            elif j == s+1:
                for i in range(2*s+3):
                    if i > s+1 and i != 2*s+2:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '7':
        for j in range(s+2):
            if j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            elif j != 0:
                for i in range(2*s+3):
                    if i == 0:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
            else:
                for i in range(2*s+3):
                    lst[i] += ' '
    elif a == '8':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            elif j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    elif a == '9':
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i < s+1 and i != 0:
                        lst[i] += '|'
                    else:
                        lst[i] += ' '
            elif j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    else:
        for j in range(s+2):
            if j == 0:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            elif j == s+1:
                for i in range(2*s+3):
                    if i == 0 or i == s+1 or i == 2*s+2:
                        lst[i] += ' '
                    else:
                        lst[i] += '|'
            else:
                for i in range(2*s+3):
                    if i == 0 or i == 2*s+2:
                        lst[i] += '-'
                    else:
                        lst[i] += ' '
    
    for l in range(2*s+3):
        lst[l] += ' '
for i in lst:
    print(''.join(i))