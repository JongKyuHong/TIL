import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
Q = int(input())
S = [0]
for i in range(1, N):
    if lst[i-1] > lst[i]:
        S.append(S[-1]+1)
    else:
        S.append(S[-1])
for _ in range(Q):
    x, y = map(int, input().split())
    print(S[y-1] - S[x-1])