t = int(input())

for _ in range(t):
    s,e = input().split()
    count_1 = 0
    count_0 = 0
    for i in range(len(e)):
        if e[i] != s[i] and e[i] == '1':
            count_1 += 1
        elif e[i] != s[i] and e[i] == '0':
            count_0 += 1
    print(max(count_1,count_0))
