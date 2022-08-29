import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())

value = a*b
target = int(math.sqrt(value)) + 1
target2 = target
flag = 0
res = sys.maxsize
res1, res2 = 0, 0

while 1:
    for i in range(target, -1, -1):
        if i * target2 == value:
            if i + target2 < res:
                res = i+target2
                res1 = i
                res2 = target2
                break
    if i == 0:
        break
    target2 += 1

print(res1, res2)