import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

if a==b==c:
    print(10000+1000*a)
elif a==b:
    print(1000+100*a)
elif b==c:
    print(1000+100*b)
elif a==c:
    print(1000+100*a)
elif a!=b and b!=c and a!=c:
    m=max(a,b,c)
    print(m*100)
    