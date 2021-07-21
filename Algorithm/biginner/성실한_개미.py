array = []

for _ in range(10):
    array.append(list(map(int,input().split())))
print()
x,y = 1,1
array[x][y] = 9
while 1:
    if array[x][y+1] == 0:
        y += 1
        array[x][y] = 9
        if array[x][y+1] == 1  and array[x+1][y] == 2:
            array[x+1][y] = 9
            break
    elif array[x+1][y] == 0:
        x += 1
        array[x][y] = 9
        if array[x+1][y] == 2:
            array[x+1][y] = 9
            break
    elif array[x+1][y] == 1 and array[x][y+1] == 1:
        break
for i in array:
    for j in i:
        print(j,end=' ')
    print()
    