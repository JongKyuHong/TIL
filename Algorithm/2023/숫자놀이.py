import sys
input = sys.stdin.readline

M, N = map(int, input().split())
dic = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
lst = []
for i in range(M, N+1):
    tmp = ''
    for j in str(i):
        tmp += dic[int(j)]
        tmp += ' '
    lst.append([tmp, i])
lst.sort()

cnt = 0
for i in lst:
    print(i[1],end='')
    cnt += 1
    if cnt == 10:
        print()
        cnt = 0
    else:
        print(' ',end='')