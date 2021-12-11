n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array.sort()

start_point = array[0][0] + array[0][1]
for i in range(1,n):
    if start_point > array[i][0]:
        start_point += array[i][1]
    else:
        start_point = array[i][0] + array[i][1]
print(start_point)