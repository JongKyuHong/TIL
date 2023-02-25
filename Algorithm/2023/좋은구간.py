import sys
input = sys.stdin.readline

L = int(input())
lst = list(map(int, input().split()))
lst.sort()
n = int(input())
start, end = 0, 0
for i in lst:
    if i < n:
        start = i
    elif i > n and end == 0:
        end = i
    elif i == n:
        print(0)
        exit()
cnt = 0

while start < n:
    start += 1
    for i in range(n, end):
        if start == i:
            continue
        #print(start, i)
        cnt += 1
print(cnt)