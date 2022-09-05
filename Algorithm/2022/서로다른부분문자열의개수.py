import sys
input = sys.stdin.readline

S = input().rstrip()
idx = 0
gap = 1
res = set()
while gap < len(S):
    while idx < len(S):
        res.add(S[idx:idx+gap])
        idx += 1
    gap += 1
    idx = 0
print(res)