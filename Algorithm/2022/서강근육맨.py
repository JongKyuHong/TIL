import sys
input = sys.stdin.readline
n = int(input())
muscle = list(map(int, input().split()))
muscle.sort()
res = 0
if n % 2:
    res = muscle.pop()
    while muscle:
        v1 = muscle.pop(0)
        v2 = muscle.pop(-1)
        res = max(res, v1+v2)
    print(res)
else:
    while muscle:
        v1 = muscle.pop(0)
        v2 = muscle.pop(-1)
        res = max(res, v1+v2)
    print(res)

