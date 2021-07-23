n = int(input())
array = [[0]*19 for _ in range(19)]
for _ in range(n):
    x,y = map(int,input().split())
    if array[x-1][y-1] != 1:
        array[x-1][y-1] += 1
    else:
        continue
for i in array:
    for j in i:
        print(j, end=' ')
    print()