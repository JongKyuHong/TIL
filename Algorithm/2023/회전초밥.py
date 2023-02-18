import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
sushi = sushi + sushi[:k-1]
max_v = 0
start, end = 0, 0
tmp = {c:1}
while start < N:
    while end < start+k:
        if sushi[end] not in tmp:
            tmp[sushi[end]] = 1
        else:
            tmp[sushi[end]] += 1
        end += 1
    max_v = max(max_v, len(tmp))
    tmp[sushi[start]] -= 1
    if tmp[sushi[start]] == 0:
        del tmp[sushi[start]]
    start += 1
print(max_v)