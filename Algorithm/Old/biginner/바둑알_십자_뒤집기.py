array = []

for _ in range(19):
    array.append(list(map(int,input().split())))
n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int,input().split())))

for a,b in m:
    for i in range(19):
        if array[i][b-1] == 1:
            array[i][b-1] = 0
        else:
            array[i][b-1] = 1
    for i in range(19):
        if array[a-1][i] == 1:
            array[a-1][i] = 0
        else:
            array[a-1][i] = 1
    

for i in array:
    for j in i:
        print(j, end=' ')
    print()