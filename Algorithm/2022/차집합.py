from collections import defaultdict
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []
arr = defaultdict(int)
for i in A:
    arr[i] += 1
for i in B:
    arr[i] -= 1

for k, v in arr.items():
    if v == 1:
        res.append(k)

if res:
    res.sort()
    print(len(res))
    print(*res)
else:
    print(0)