import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
target = 0
v = m-1
for i in range(m):
    target += lst[i]*(a**v)
    v -= 1

res = []
while 1:
    q,r = divmod(target, b)
    res.append(r)
    if q >= b:
        target = q
    else:
        res.append(q)
        break
        
print(*res[::-1])

