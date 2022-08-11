import sys

input = sys.stdin.readline
n = int(input())
num = []
sums = []
s = 0
for n in input().split():
    n = int(n)
    s += n
    sums.append(s)
    num.append(n)

i = 0
r=  0
while i < n-1:
    r += (s-sums[i])*num[i]
    i += 1
print(r)