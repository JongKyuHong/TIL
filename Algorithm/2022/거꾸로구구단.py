import sys

input = sys.stdin.readline

n, k = map(int, input().split())

res = []
for i in range(1,k+1):
    res.append(int(str(n*i)[::-1]))

print(max(res))