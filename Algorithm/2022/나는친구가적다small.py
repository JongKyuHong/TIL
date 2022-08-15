S = input()
s = ''
for i in S:
    if i.isalpha():
        s += i

k = input()
idx, flag = 0, 0
for i in s:
    target = k[idx]
    if i == target:
        idx += 1
        if idx == len(s):
            flag = 1
            break
    else:
        idx = 0

if flag:
    print(1)
else:
    print(0)