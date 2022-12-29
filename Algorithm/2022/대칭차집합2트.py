from collections import defaultdict
import sys
input = sys.stdin.readline

dic = defaultdict(int)
a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in A:
    dic[i] += 1
for i in B:
    dic[i] -= 1
for k, v in dic.items():
    if v == 0:
        pass
    else:
        cnt += 1
print(cnt)