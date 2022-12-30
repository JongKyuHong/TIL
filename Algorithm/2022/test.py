import sys
input = sys.stdin.readline

x, y = map(int, input().split())

def gcd(x, y):
    if x > y:
        x, y = y, x
    while y:
        x, y = y, x%y
    return x
print(x+y-gcd(x,y))