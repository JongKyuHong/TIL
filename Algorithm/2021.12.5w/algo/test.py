n = int(input())
data = sorted(list(map(int, input().split())))
result = 0

for i in reversed(range(1, 1001)):
    tmp1 = list(filter(lambda x: x >= i, data))
    if len(tmp1) >= i:
        result = i
        break

print(result)