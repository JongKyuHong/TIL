n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a1 = sorted(a[1:])
    b1 = sorted(b[1:])
    i = 0
    winner = 0
    while a1 and b1:
        a2 = a1.pop()
        b2 = b1.pop()
        if a2 == b2:
            i += 1
            continue
        elif a2 > b2:
            winner = 1
            break
        else:
            winner = 2
            break
    if winner == 1:
        print('A')
    elif winner == 2:
        print('B')
    else:
        if a1:
            print('A')
        elif b1:
            print('B')
        else:
            print('D')



