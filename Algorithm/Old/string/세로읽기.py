array = []
for _ in range(5):
    array.append(input())
for i in range(max([len(e) for e in array])):
    for j in range(5):
        if i < len(array[j]):
            print(array[j][i],end='')



