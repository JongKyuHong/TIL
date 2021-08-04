n = int(input())
cre = sorted(list(map(int,input().split())),reverse=True)
m = int(input())
boxs = sorted(list(map(int,input().split())),reverse=True)

if cre[0] < boxs[0]:
    print(-1)
else:
    count = 0
    while boxs:
        count += 1
        for i in cre:
            if not boxs:
                break
            else:
                for j in range(len(boxs)):
                    if boxs[j] <= i:
                        boxs.pop(j)
                        break
    print(count)