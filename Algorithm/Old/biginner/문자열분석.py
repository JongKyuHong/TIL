import sys

while 1:
    n = sys.stdin.readline().rstrip('\n')
    if not n:
        break
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    for i in n:
        if i.islower():
            cnt1 += 1
        elif i.isupper():
            cnt2 += 1
        elif i.isdigit():
            cnt3 += 1
        elif i.isspace():
            cnt4 += 1
    print(f'{cnt1} {cnt2} {cnt3} {cnt4}')