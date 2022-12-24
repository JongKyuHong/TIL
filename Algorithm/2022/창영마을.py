import sys
input = sys.stdin.readline

words = input().rstrip()
lst = [1,0,0]
for word in words:
    if word == 'A':
        if lst[0]:
            lst[0] = 0
            lst[1] = 1
        elif lst[1]:
            lst[0] = 1
            lst[1] = 0
    elif word == 'B':
        if lst[1]:
            lst[1] = 0
            lst[2] = 1
        elif lst[2]:
            lst[2] = 0
            lst[1] = 1
    else:
        if lst[2]:
            lst[2] = 0
            lst[0] = 1
        elif lst[0]:
            lst[0] = 0
            lst[2] = 1
for i in range(3):
    if lst[i]:
        print(i+1)

