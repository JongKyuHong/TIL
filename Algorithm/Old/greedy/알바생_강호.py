n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)
sum = 0
for i in range(n):
    if array[i]-i <0:
        sum += 0
    else:
        sum += array[i]-i
print(sum)