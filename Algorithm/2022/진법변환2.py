import sys 
input = sys.stdin.readline

n, b = map(int, input().split())
res = []
while n != 0:
    n, r = divmod(n, b)
    if r >= 10:
        res.insert(0, chr(r+55))
    else:
        res.insert(0, str(r))
print(''.join(res))