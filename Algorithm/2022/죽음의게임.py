import sys
input = sys.stdin.readline

n, k = map(int, input().split())
parent = [0]*(n+1)

for i in range(n):
    a = int(input())
    parent[i] = a
cnt = 0
idx = 0
while cnt < n:
    cnt += 1
    idx = parent[idx]
    if idx == k:
        print(cnt)
        exit()
print(-1)