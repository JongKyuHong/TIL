for _ in range(int(input())):
    string = list(input().split())
    for i in range(len(string)):
        if i == 0:
            res = string[i][0].upper() + string[i][1:]
            print(res, end=' ')
        else:
            print(string[i],end=' ')