import math

n = int(input())
string = list(input())

recent = string[0]
cnt = 0
for i in range(1,n):
    if string[i] == recent:
        continue
    else:
        cnt += 0.5
        recent = string[i]
print(math.ceil(cnt)+1)