array = []

for _ in range(10):
    array.append(list(map(int,input().split())))
x,y = 1,1
array[x][y] = 9
while 1:
    if array[x][y] == 2:
        array[x][y] = 9
        break
    elif array[x+1][y] == 1 and array[x][y+1] == 1:
        array[x][y] = 9
        break
    array[x][y] = 9
    if array[x][y+1] == 1:
        x += 1
    elif array[x+1][y] == 1:
        y += 1
    else:
        y +=1
for i in array:
    for j in i:
        print(j,end=' ')
    print()
    