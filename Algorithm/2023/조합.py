import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a, b = 1, 1
for i in range(M):
    a *= (N-i)
for i in range(1,M+1):
    b *= i
print(a/b)
