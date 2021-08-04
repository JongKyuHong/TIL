t = int(input())

# for _ in range(t):
#     n = int(input())
#     array = []
#     count = 0
#     for _ in range(n):
#         array.append(list(map(int,input().split())))
#     for a,b in array:
#         for i in range(len(array)):
#             if a > array[i][0] and b > array[i][1]:
#                 count += 1
#                 break
#     print(n-count)

# for _ in range(t):
#     n = int(input())
#     array = []
#     count = 0
#     for _ in range(n):
#         array.append(list(map(int,input().split())))
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i][0] > array[j][0] and array[i][1] > array[j][1]:
#                 count += 1
#                 array.remove(array[i])
#                 break
#     print(n-count)

for _ in range(t):
    n = int(input())
    array = []
    count = 1
    for _ in range(n):
        array.append(list(map(int,input().split())))
    array.sort(key=lambda x: x[0])
    mina = array[0][1]

    for i in range(1,n):
        if array[i][1] < mina:
            mina = array[i][1]
            count += 1
    print(count)