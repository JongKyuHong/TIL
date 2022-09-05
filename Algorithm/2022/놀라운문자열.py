import sys
input = sys.stdin.readline

while 1:
    S = input().rstrip()
    if S == '*':
        break
    n = len(S)
    idx, gap = 0, 1
    flag = 1
    while gap < n:
        a_dict = {}
        for i in range(n-gap):
            ans = S[i] + S[i+gap]
            if ans in a_dict:
                flag = 0
                break
            else:
                a_dict[ans] = 1
        gap += 1
        if flag == 0:
            break
    print(a_dict)
    if flag:
        print(f'{S} is surprising.')
    else:
        print(f'{S} is NOT surprising.')

