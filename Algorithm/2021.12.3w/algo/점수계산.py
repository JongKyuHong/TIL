array = [(int(input()),i) for i in range(8)]
array.sort(key=lambda x: x[0], reverse=True)
sum,sum_list = 0, []
for i in range(5):
    sum += array[i][0]
    sum_list.append(array[i][1]+1)
print(sum)
sum_list.sort()
print(*sum_list)
