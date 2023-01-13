import sys
input = sys.stdin.readline

N, K = map(int, input().split())
inp = list(map(int, input().split()))
lst = []
for i in range(1, N):
    lst.append(inp[i]-inp[i-1])
lst.sort()
print(sum(lst[:N-K]))