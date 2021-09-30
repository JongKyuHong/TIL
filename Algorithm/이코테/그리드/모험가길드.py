n = int(input())
array = sorted(list(map(int, input().split())))
res = 0
cnt = 0
for i in array:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)

