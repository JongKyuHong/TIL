import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 
S = [0] * 1000001
max_len = 0

for _ in range(N):
    g,x = map(int, input().split())
    max_len = max(max_len, x)
    S[x] = g

summary = 0
max_v = 0

for i in range(K, max_len-K+1):
    if i == K:
        for j in range(1, K+1):
            summary += S[i-j]
        for j in range(1, K+1):
            summary += S[i+j]
    else:
        summary += S[i+K]
    max_v = max(max_v, summary)
    summary -= S[i-K]
print(max_v)