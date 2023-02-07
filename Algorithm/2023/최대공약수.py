import sys
input = sys.stdin.readline

def gcd(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        x, y = y, x%y
    return x

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
l1, l2 = 1, 1
for i in lst:
    l1 *= i
for i in lst2:
    l2 *= i    
result = gcd(l1, l2)
if result > 100000000:
    print(str(result)[-9:])
else:
    print(result)
