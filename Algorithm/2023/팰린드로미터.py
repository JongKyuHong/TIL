import sys
input = sys.stdin.readline

while 1:
    num = input().rstrip()
    if num == '0':
        break
    cnt = 0
    while 1:
        if num == num[::-1]:
            break
        else:
            len_ = len(num)
            tmp = str(int(num)+1)
            num = tmp.zfill(len_)
            cnt += 1
    print(cnt)
    print(num)
    


