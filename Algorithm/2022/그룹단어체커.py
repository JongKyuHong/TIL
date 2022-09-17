n = int(input())
res = 0
for _ in range(n):
    words = {}
    a = list(input())
    flag = 0
    current = ''
    for i in a:
        if i in words:
            if current != i:
                flag = 1
                break
        else:
            words[i] = 1
        current = i
    if flag == 0:
        res += 1
print(res)