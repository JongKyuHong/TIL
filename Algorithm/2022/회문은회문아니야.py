import sys
input = sys.stdin.readline

S = input().rstrip()
n = len(S)
if S == S[0]*n:
    print(-1)
elif S == S[::-1]:
    print(n-1)
else:
    print(n)
