a,b,c=map(int, input().split())
res = 1
if (a % 2 and b % 2 and c % 2) or a%2 == 0 and b%2 == 0 and c%2 == 0:
    print(a*b*c)
else:
    if a % 2:
        res *= a
    if b % 2:
        res *= b
    if c % 2:
        res *= c
    print(res)