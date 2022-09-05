import sys
input = sys.stdin.readline

S = input().rstrip()
res = []
res.append(S)
for i in range(1, len(S)):
    res.append(S[i:])
res.sort()
for i in res:
    print(i)
