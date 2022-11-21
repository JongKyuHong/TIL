import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = ['']*n
idx = 0
for i in range(k):
    S, word = input().rstrip().split()
    if i == 0:
        idx = int(S)
        while 1:
            idx %= n
            if idx < n:
                break
        lst[idx] = word
    else:
        idx -= int(S)
        while 1:
            idx %= n
            if idx < n:
                break
        
        if not lst[idx]:
            if word not in lst:
                lst[idx] = word
            else:
                print('!')
                exit()
        else:
            if lst[idx] != word:
                print('!')
                exit()

cnt = n
while cnt > 0:
    if not lst[idx]:
        print('?',end='')
    else:
        print(lst[idx],end='')
    idx += 1
    idx %= n
    cnt -= 1
    