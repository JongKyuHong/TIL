n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
if len(array) == 1:
    print(1)
    exit(0)
else:
    count1=0
    target = sorted(array,key=lambda x:x[1])[0]
    for i in array:
        if i[0] < target[1]:
            count1 += 1
        else:
            count1 = len(array)
            break
    array.sort()
    print(array)
    count = 1
    for i in range(count1):
        result = [array[i]]
        j = i+1
        while j<len(array):
            if array[i][1] <= array[j][0]:
                result.append(array[j])
                i=j
                j+=1
            else:
                j += 1
        count = max(count,len(result))
    print(count)

# 
# array.sort()

# array2 = []
# i = 0
# while 1:
#     if array[i][0] < target[1]:
#         array2.append(array[i])
#     else:
#         break
#     i += 1
# print(array2)
# count = 1
# for i in array2:
#     for j in range(len(array)):
#         if i[1] < array[j][0]:
#             count += 1

