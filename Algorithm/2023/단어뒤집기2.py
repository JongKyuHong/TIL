import sys
input = sys.stdin.readline

words = input().rstrip()
answer = ''
tmp = ''
flag = 0
for w in words:
    if w == '<':
        answer += tmp[::-1]
        tmp = ''
        flag = 1
        answer += w
    elif w == '>':
        flag = 0
        answer += w
    elif not flag:
        if w == ' ':
            answer += tmp[::-1]
            answer += ' '
            tmp = ''
        else:
            tmp += w
    elif flag:
        answer += w
answer += tmp[::-1]
print(answer)