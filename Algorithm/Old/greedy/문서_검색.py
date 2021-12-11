array = input()
target = input()
count = 0
i =0
while i<len(array):
    if array[i] == target[0]:
        if array[i:len(target)+i] == target:
            count += 1
            i += len(target)
            continue
    i += 1
print(count)