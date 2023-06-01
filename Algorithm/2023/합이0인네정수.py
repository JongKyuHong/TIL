import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
ab = {}
for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        v = a+b
        if v not in ab:
            ab[v] = 1
        else:
            ab[v] += 1
res = 0
for c in C:
    for d in D:
        v = -1*(c+d)
        if v in ab:
            res += ab[v]
print(res)