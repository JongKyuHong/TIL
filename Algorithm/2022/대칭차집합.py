import sys
input = sys.stdin.readline

a, b = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
for i in A:
    if i not in B:
        res += 1

for i in B:
    if i not in A:
        res += 1
print(res)