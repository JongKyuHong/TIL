n,k = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
array2 = []
for i in range(len(array)):
    if array[i] < k:
        array2.append(array[i])
    elif array[i] == k:
        print(1)
        exit(0)
array2.sort(reverse=True)
count = 0
for i in array2:
    count += k // i
    k %= i
print(count)