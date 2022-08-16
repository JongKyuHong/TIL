n = int(input())

alpha = {}
res = []
tt = '1'

for _ in range(n):
    string = list(input().split())
    res.append(string)
    flag = 0
    for i in range(len(string)):
        if string[i][0].lower() not in alpha:
            string[i][0] = '['+string[i][0]+']'
            alpha[target.lower()] = [string,string[i][0], 0]
            print(alpha,'알파')
            exit()
            flag = 1
            break

    if flag:
        continue
    for i in range(len(string)):
        for j in range(len(string[i])):
            if string[i][j].lower() not in alpha:
                target = string[i][j]
                alpha[target.lower()] = [string, string[i][j], j]
                flag = 1
                break
        if flag:
            break
    
    if flag:
        continue

    alpha[tt] = [string, tt]
    tt = str(int(tt)+1)

print(alpha,'alpha')

for key, value in alpha.items():
    flag = 0
    for v in value[0]:
        for i in v:
            for j in i:
                if j == value[1] and flag == 0:
                    flag = 1
                    print(f'[{j}]',end='')
                else:
                    print(j,end='')
        print(end=' ')
    print()