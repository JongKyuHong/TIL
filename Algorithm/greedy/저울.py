import sys

n = int(input())
array = list(map(int,sys.stdin.readline().split()))
array.sort()
result = 0
for i in range(len(array)):
    if result + 1 >= array[i]:
        result += array[i]
    else:
        break
print(result)


