import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
S = [0]
for i in lst:
    S.append(S[-1]+i)

for _ in range(Q):
    l, r = map(int, input().split())
    print(S[r] - S[l-1])
