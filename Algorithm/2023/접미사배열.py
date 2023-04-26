import sys
input = sys.stdin.readline

S = input().rstrip()
res = []
for i in range(len(S)):
    res.append(S[i:])
res.sort()
for i in res:
    print(i)