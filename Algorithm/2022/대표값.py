import sys
input = sys.stdin.readline

res = 0
cnt = {}
for _ in range(10):
    t = int(input())
    res += t
    if t in cnt:
        cnt[t] += 1
    else:
        cnt[t] = 1
max_v = 0
max_k = 0
for key, value in cnt.items():
    if max_v < value:
        max_k = key
        max_v = value
print(res//10)
print(max_k)