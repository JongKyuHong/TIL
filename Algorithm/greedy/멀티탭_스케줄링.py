# n,k = map(int,input().split())

# array = list(map(int,input().split()))
# array2 = []
# count = 0
# flag = 0
# for i in range(len(array)):
#     if array[i] not in array2:
#         if len(array2) < n:
#             array2.append(array[i])
#         else:
#             for j in array2:
#                 if j not in array[i:i+n]:
#                     pop_index = array2.index(j)
#                     array2.insert(pop_index,array[i])
#                     array2.pop(pop_index+1)
#                     count += 1
#                     flag = 1
#                     break
#             if flag == 0:
#                 for j in array2:
#                     sum = 0
#                     sum = max(sum,array[i:].index(j))
#             # array[sum2]
#             # pop_index = array2.index(j)
#             # array2.insert(pop_index,array[i])
#             # array2.pop(pop_index+1)
#             # count += 1
#             # break
# print(count)

a = [1,2,3,4,5]
print(a[3:].index(3))
