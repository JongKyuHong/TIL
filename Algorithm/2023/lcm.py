import sys
input = sys.stdin.readline

def gcd(x, y):
    if y > x:
        x, y = y, x
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y//gcd(x, y)

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(lcm(a, b))
