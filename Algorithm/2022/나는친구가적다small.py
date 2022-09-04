S = input()

k = input()
idx, flag = 0, 0
for i in S:
    if i.isalpha():
        target = k[idx]
        if i == target:
            idx += 1
            if idx == len(k):
                flag = 1
                break
        else:
            idx = 0

if flag:
    print(1)
else:
    print(0)