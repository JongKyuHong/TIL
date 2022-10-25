import sys
input = sys.stdin.readline

while 1:
    n = input().rstrip()
    if n == '0':
        break
    len_n = len(n)
    answer = len_n+1
    for i in n:
        if i == '0':
            answer += 4
        elif i == '1':
            answer += 2
        else:
            answer += 3
    print(answer)
