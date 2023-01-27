from itertools import permutations
import sys
input = sys.stdin.readline

A, B = input().split()
B = int(B)
ans = -1
for p in list(map(''.join, list(permutations(A)))):
    first = p[0]
    p = int(p)
    if B >= p and first != '0':
        ans = max(ans, p)
print(ans)