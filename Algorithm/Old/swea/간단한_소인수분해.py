t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    a,b,c,d,e = 0,0,0,0,0
    while n % 2 == 0:
        a += 1
        n //= 2
    while n % 3 == 0:
        b += 1
        n //= 3
    while n % 5 == 0:
        c += 1
        n //= 5
    while n % 7 == 0:
        d += 1
        n //= 7
    while n % 11 == 0:
        e += 1
        n //= 11
    print(f'#{test_case} {a} {b} {c} {d} {e}')

