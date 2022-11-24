import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    data = input().rstrip().split()
    for i in range(len(data)):
        if data[i][0].upper() not in arr:
            arr.append(data[i][0].upper())
            data[i] = '['+data[i][0]+']'+data[i][1:]
            print(' '.join(data))
            break
    else:
        for i in range(len(data)):
            flag = 0
            for j in range(len(data[i])):
                if data[i][j].upper() not in arr:
                    arr.append(data[i][j].upper())
                    data[i] = data[i][:j] + '[' + data[i][j] + ']' + data[i][j+1:]
                    print(' '.join(data))
                    flag = 1
                    break
            if flag:
                break
        else:
            print(' '.join(data))