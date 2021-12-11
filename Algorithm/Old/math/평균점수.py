nums = [int(input()) for _ in range(5)]
res = 0
for i in nums:
    if i >= 40:
        res += i
    else:
        res += 40
print(int(res/5))


