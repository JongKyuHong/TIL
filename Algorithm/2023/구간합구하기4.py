import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(S[-1]+nums[i])
for _ in range(M):
    i, j = map(int, input().split())
    print(S[j]-S[i-1])