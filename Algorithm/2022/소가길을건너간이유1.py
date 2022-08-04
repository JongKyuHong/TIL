n = int(input())
dict = {}
res = 0
for _ in range(n):
    cow, num = map(int, input().split())
    if cow not in dict:
        dict[cow] = num
    else:
        if dict[cow] != num:
            res += 1
            dict[cow] = num
print(res)
