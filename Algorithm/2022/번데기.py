A = int(input())
T = int(input())
target = int(input())

n = 2
idx = 0
bun_list = []
while 1:
    bun_list += [0,1,0,1]
    for i in range(n):
        bun_list.append(0)
    for i in range(n):
        bun_list.append(1)

    if len(bun_list) // 2 >= T:
        for i in bun_list:
            if i == target:
                T -= 1
                if T == 0:
                    print(idx)
                    exit()
            idx +=1
            idx %=A
    else:
        n += 1